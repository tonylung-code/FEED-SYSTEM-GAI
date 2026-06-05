from __future__ import annotations

import os
import json
import re
from functools import lru_cache
from typing import Any

import numpy as np
import requests

from ui_paths import VECTOR_DATA_DIR


VALID_SOURCES = ("FANUC", "HIWIN", "PMI", "All")
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"
DEFAULT_MODEL = "llama3.2:latest"
USE_SEMANTIC_SEARCH = os.environ.get("FEED_UI_SEMANTIC_SEARCH", "1") != "0"
SEMANTIC_THRESHOLD = float(os.environ.get("FEED_UI_SEMANTIC_THRESHOLD", "0.35"))
EXACT_MATCH_SCORE = 1.0
STRUCTURED_MATCH_SCORE = 0.95
MAX_CONTEXT_LENGTH = 1200

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")


@lru_cache(maxsize=1)
def _embedding_model():
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer("BAAI/bge-m3", local_files_only=True)


@lru_cache(maxsize=1)
def _reranker_model():
    from sentence_transformers import CrossEncoder

    return CrossEncoder("BAAI/bge-reranker-v2-m3", local_files_only=True)


@lru_cache(maxsize=8)
def _load_npz(source: str):
    npz_path = VECTOR_DATA_DIR / f"{source}_final_chunks.npz"
    if not npz_path.exists():
        raise FileNotFoundError(f"Vector data not found: {npz_path}")
    return np.load(npz_path, allow_pickle=True)


@lru_cache(maxsize=8)
def _load_json_chunks(source: str) -> list[dict[str, Any]]:
    json_path = VECTOR_DATA_DIR / f"{source}_final_chunks.json"
    if not json_path.exists():
        return []

    try:
        with json_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception:
        return []

    return data if isinstance(data, list) else []


def _as_text_list(values: Any) -> list[str]:
    return [str(value) for value in values]


def _source_file(source: str) -> str:
    return f"{source}_final_chunks.json"


def _metadata_page(item: dict[str, Any]) -> Any:
    metadata = item.get("metadata")
    if not isinstance(metadata, dict):
        metadata = {}
    return item.get("page") or metadata.get("source_page") or metadata.get("page")


def _load_records(source: str) -> list[dict[str, Any]]:
    data = _load_npz(source)
    if "embeddings" not in data or "texts" not in data:
        raise KeyError(f"Invalid vector file for {source}: expected embeddings/texts arrays")

    texts = _as_text_list(data["texts"])
    json_chunks = _load_json_chunks(source)
    records: list[dict[str, Any]] = []
    for idx, text in enumerate(texts):
        item = json_chunks[idx] if idx < len(json_chunks) and isinstance(json_chunks[idx], dict) else {}
        records.append(
            {
                "content": text,
                "score": 0.0,
                "score_type": "none",
                "source": source,
                "source_file": _source_file(source),
                "source_page": _metadata_page(item),
                "chunk_id": idx,
                "match_reason": "unscored",
            }
        )
    return records


def _dedupe_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    best_by_key: dict[tuple[str, int], dict[str, Any]] = {}
    for candidate in candidates:
        key = (str(candidate.get("source_file")), int(candidate.get("chunk_id", -1)))
        current = best_by_key.get(key)
        if current is None or _candidate_rank(candidate) > _candidate_rank(current):
            best_by_key[key] = candidate
    return sorted(best_by_key.values(), key=_candidate_rank, reverse=True)


def _candidate_rank(candidate: dict[str, Any]) -> tuple[int, float]:
    priority = {
        "exact": 4,
        "structured": 3,
        "semantic_cosine": 2,
        "keyword_count": 1,
    }.get(str(candidate.get("score_type")), 0)
    return priority, float(candidate.get("score", 0.0))


def _keyword_tokens(question: str) -> list[str]:
    raw_tokens = re.findall(r"[A-Za-z0-9]+|[\u4e00-\u9fff]+", question.lower())
    tokens: list[str] = []
    for token in raw_tokens:
        if re.fullmatch(r"[\u4e00-\u9fff]+", token) and len(token) > 4:
            tokens.extend(re.findall(r"外徑|直徑|導程|型號|規格|馬達|螺桿|推薦|使用|場景|不變|\d+", token))
        else:
            tokens.append(token)
    return [token for token in tokens if token.strip()]


def _keyword_score(text: str, tokens: list[str]) -> int:
    haystack = text.lower()
    return sum(haystack.count(token) for token in tokens)


def _keyword_search_records(
    records: list[dict[str, Any]],
    question: str,
    top_k: int = 3,
    match_reason: str = "keyword_fallback",
) -> list[dict[str, Any]]:
    tokens = _keyword_tokens(question)

    if not tokens:
        return []

    scored = []
    for record in records:
        score = _keyword_score(str(record["content"]), tokens)
        if score <= 0:
            continue
        item = dict(record)
        item.update({"score": float(score), "score_type": "keyword_count", "match_reason": match_reason})
        scored.append(item)

    scored.sort(key=lambda item: float(item["score"]), reverse=True)
    return scored[:top_k]


def _keyword_search_texts(texts: list[str], question: str, top_k: int = 3) -> list[str]:
    records = [{"content": text, "chunk_id": idx} for idx, text in enumerate(texts)]
    return [item["content"] for item in _keyword_search_records(records, question, top_k=top_k)]


def _has_calc_context(calc_context: dict[str, Any] | None) -> bool:
    if not calc_context:
        return False
    return calc_context.get("status") != "calculation unavailable" and any(
        calc_context.get(key)
        for key in (
            "guide",
            "dynamic_load",
            "torque",
            "recommendations_summary",
            "motor_summary",
            "safety_summary",
            "inertia_summary",
        )
    )


def _is_calculation_query(question: str) -> bool:
    return any(
        term in question
        for term in (
            "計算",
            "推薦",
            "扭矩",
            "動負荷",
            "負荷",
            "剛性",
            "慣量",
            "外徑",
            "導程",
            "馬達",
            "安全",
            "臨界轉速",
            "挫曲",
            "壓縮力",
            "拉伸力",
            "符合",
            "足夠",
            "夠嗎",
        )
    )


def _is_rag_query(question: str, structured_query: dict[str, Any]) -> bool:
    if structured_query.get("has_structured_terms"):
        return True
    return any(
        term in question.upper()
        for term in (
            "HIWIN",
            "PMI",
            "FANUC",
            "規格",
            "型錄",
            "資料",
            "螺桿",
            "滾珠",
            "導程",
            "外徑",
            "SERVO",
            "MOTOR",
            "剛性",
            "精度",
            "負載",
        )
    )


def _route_query(
    question: str,
    structured_query: dict[str, Any] | None = None,
    calc_context: dict[str, Any] | None = None,
) -> dict[str, str]:
    normalized = question.strip().lower()
    greetings = {"hi", "hello", "你好", "您好", "哈囉", "哈啰"}
    tests = {"test", "測試", "测试"}
    thanks = {"謝謝", "谢谢", "thanks", "thank you", "感謝"}
    structured_query = structured_query or _parse_structured_query(question)

    if normalized in greetings:
        return {"route": "greeting", "answer": "您好，我可以協助查詢進給系統選型、規格或馬達相關問題。"}
    if normalized in tests:
        return {"route": "test", "answer": "系統測試正常。請輸入規格、型號或選型問題，我會再進行資料查詢。"}
    if normalized in thanks:
        return {"route": "general_chat", "answer": ""}
    if _has_calc_context(calc_context) and _is_calculation_query(question):
        return {"route": "calculation_qa", "answer": ""}
    if not _is_rag_query(question, structured_query):
        return {"route": "general_chat", "answer": ""}
    return {"route": "rag", "answer": ""}


def _parse_structured_query(question: str) -> dict[str, Any]:
    model_matches = [
        item
        for item in re.findall(r"\b[A-Z]{1,6}(?:-[A-Z0-9]{1,12})+\b", question.upper())
        if re.search(r"\d", item)
    ]

    diameter = None
    diameter_patterns = [
        r"(?:外徑|直徑|公稱外徑|螺桿外徑|Ø|Φ)\s*[:：]?\s*(\d+(?:\.\d+)?)",
        r"(\d+(?:\.\d+)?)\s*mm\s*(?:外徑|直徑)",
    ]
    for pattern in diameter_patterns:
        match = re.search(pattern, question, flags=re.IGNORECASE)
        if match:
            diameter = float(match.group(1))
            break

    lead = None
    lead_patterns = [
        r"(?:導程|lead)\s*[:：]?\s*(\d+(?:\.\d+)?)",
        r"(\d+(?:\.\d+)?)\s*mm\s*(?:導程|lead)",
    ]
    for pattern in lead_patterns:
        match = re.search(pattern, question, flags=re.IGNORECASE)
        if match:
            lead = float(match.group(1))
            break

    return {
        "models": sorted(set(model_matches)),
        "diameter": diameter,
        "lead": lead,
        "has_structured_terms": bool(model_matches or diameter is not None or lead is not None),
    }


def _number_variants(value: float | None) -> set[str]:
    if value is None:
        return set()
    if float(value).is_integer():
        int_value = int(value)
        return {str(int_value), f"{int_value}.0", f"Ø{int_value}", f"Φ{int_value}"}
    return {str(value)}


def _has_model_exact(text: str, model: str) -> bool:
    return re.search(rf"(?<![A-Z0-9]){re.escape(model)}(?![A-Z0-9])", text.upper()) is not None


def _structured_match_score(text: str, structured_query: dict[str, Any]) -> tuple[bool, str]:
    normalized = text.upper()
    for model in structured_query.get("models", []):
        if _has_model_exact(normalized, model):
            return True, f"exact_model:{model}"

    diameter = structured_query.get("diameter")
    lead = structured_query.get("lead")
    if diameter is None and lead is None:
        return False, ""

    has_diameter = True
    if diameter is not None:
        diameter_values = _number_variants(diameter)
        has_diameter = any(value.upper() in normalized for value in diameter_values)

    has_lead = True
    if lead is not None:
        lead_values = _number_variants(lead)
        has_lead = any(value.upper() in normalized for value in lead_values)

    has_spec_language = any(term in text for term in ("外徑", "直徑", "導程", "螺桿", "規格", "型號"))
    if has_diameter and has_lead and has_spec_language:
        return True, "structured_spec_match"

    return False, ""


def _structured_search_records(
    records: list[dict[str, Any]],
    structured_query: dict[str, Any],
    top_k: int = 3,
) -> list[dict[str, Any]]:
    matches = []
    for record in records:
        matched, reason = _structured_match_score(str(record["content"]), structured_query)
        if not matched:
            continue

        item = dict(record)
        score = EXACT_MATCH_SCORE if reason.startswith("exact_model") else STRUCTURED_MATCH_SCORE
        item.update({"score": score, "score_type": "exact" if reason.startswith("exact_model") else "structured", "match_reason": reason})
        matches.append(item)

    return _dedupe_candidates(matches)[:top_k]


def _semantic_search_records(
    source: str,
    records: list[dict[str, Any]],
    question: str,
    top_k: int = 3,
) -> list[dict[str, Any]]:
    data = _load_npz(source)
    embeddings = data["embeddings"]

    from sklearn.metrics.pairwise import cosine_similarity

    query_vec = _embedding_model().encode([question], normalize_embeddings=True)
    similarities = cosine_similarity(query_vec, embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in top_indices:
        score = float(similarities[idx])
        item = dict(records[int(idx)])
        item.update({"score": score, "score_type": "semantic_cosine", "match_reason": "semantic_search"})
        results.append(item)
    return results


def _search_one_source_structured(
    source: str,
    question: str,
    structured_query: dict[str, Any],
    top_k: int = 3,
) -> tuple[list[dict[str, Any]], str]:
    records = _load_records(source)
    raw_candidates: list[dict[str, Any]] = []
    search_mode = "keyword"

    structured_matches = _structured_search_records(records, structured_query, top_k=top_k)
    raw_candidates.extend(structured_matches)

    model_query = bool(structured_query.get("models"))
    exact_model_found = any(str(item.get("match_reason", "")).startswith("exact_model") for item in structured_matches)
    if model_query and not exact_model_found:
        return raw_candidates, "exact_model_only_no_match"

    if USE_SEMANTIC_SEARCH:
        try:
            semantic_matches = _semantic_search_records(source, records, question, top_k=top_k)
            raw_candidates.extend(semantic_matches)
            search_mode = "semantic"
        except Exception:
            raw_candidates.extend(_keyword_search_records(records, question, top_k=top_k))
            search_mode = "keyword_fallback_after_semantic_error"
    else:
        raw_candidates.extend(_keyword_search_records(records, question, top_k=top_k))
        search_mode = "keyword_forced"

    return _dedupe_candidates(raw_candidates), search_mode


def _passes_relevance(candidate: dict[str, Any]) -> bool:
    score_type = candidate.get("score_type")
    score = float(candidate.get("score", 0.0))
    if score_type in {"exact", "structured"}:
        return True
    if score_type == "semantic_cosine":
        return score >= SEMANTIC_THRESHOLD
    if score_type == "keyword_count":
        return score > 0
    return False


def _format_candidate_for_context(candidate: dict[str, Any]) -> str:
    return (
        f"[Source: {candidate.get('source_file')}, page: {candidate.get('source_page')}, "
        f"chunk: {candidate.get('chunk_id')}, score: {candidate.get('score')}, "
        f"match: {candidate.get('match_reason')}]\n{candidate.get('content')}"
    )


def _build_context(candidates: list[dict[str, Any]]) -> list[str]:
    return [_format_candidate_for_context(candidate) for candidate in candidates]


def _preview(text: str, limit: int = 1200) -> str:
    return text if len(text) <= limit else text[:limit] + "..."


def _search_structured_flow(
    source: str,
    question: str,
    top_k: int = 3,
    calc_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    source = source.strip()
    if source not in VALID_SOURCES:
        raise ValueError(f"Unsupported source: {source}")

    structured_query = _parse_structured_query(question)
    route = _route_query(question, structured_query=structured_query, calc_context=calc_context)
    if route["route"] != "rag":
        return {
            "route_decision": route["route"],
            "route_answer": route["answer"],
            "search_mode": "not_applicable",
            "structured_query": structured_query,
            "top_k_raw_candidates": [],
            "top_k_filtered_candidates": [],
            "final_context": [],
        }

    sources = ("FANUC", "HIWIN", "PMI") if source == "All" else (source,)
    raw_candidates: list[dict[str, Any]] = []
    modes = []
    for item in sources:
        source_candidates, mode = _search_one_source_structured(item, question, structured_query, top_k=top_k)
        raw_candidates.extend(source_candidates)
        modes.append(f"{item}:{mode}")

    raw_candidates = _dedupe_candidates(raw_candidates)
    filtered_candidates = [candidate for candidate in raw_candidates if _passes_relevance(candidate)]

    return {
        "route_decision": "rag",
        "route_answer": "",
        "search_mode": ", ".join(modes),
        "structured_query": structured_query,
        "top_k_raw_candidates": raw_candidates[:top_k],
        "top_k_filtered_candidates": filtered_candidates[:top_k],
        "final_context": _build_context(filtered_candidates[:top_k]),
    }


def simple_search(source: str, question: str, top_k: int = 3) -> list[str]:
    return [item["content"] for item in simple_search_structured(source, question, top_k=top_k)]


def simple_search_structured(source: str, question: str, top_k: int = 3) -> list[dict[str, Any]]:
    return _search_structured_flow(source, question, top_k=top_k)["top_k_filtered_candidates"]


def rerank_recall_results(contents: list[str], question: str, top_k: int = 3) -> list[str]:
    if not contents:
        return []

    try:
        pairs = [[question, content] for content in contents]
        scores = _reranker_model().predict(pairs)
        scored_chunks = list(zip(contents, scores))
        scored_chunks.sort(key=lambda item: item[1], reverse=True)
        return [chunk for chunk, _score in scored_chunks[:top_k]]
    except Exception:
        return _keyword_search_texts(contents, question, top_k=top_k)


def _source_scope_text(source: str) -> str:
    if source == "All":
        return "目前來源範圍是 All，可使用 FANUC、HIWIN、PMI 的通過門檻資料進行比較。"
    return f"目前來源範圍是 {source}。除非使用者明確要求比較，不得引用其他品牌來源資料。"


def _compact_calc_context(calc_context: dict[str, Any], source: str) -> dict[str, Any]:
    scoped = dict(calc_context or {})
    recommendations = scoped.get("recommendations_summary")
    if isinstance(recommendations, dict) and source in {"HIWIN", "PMI"}:
        scoped["recommendations_summary"] = {source: recommendations.get(source, [])}
    return scoped


def optimize_prompt(
    question: str,
    context: list[str] | str,
    calc_context: dict[str, Any],
    source: str = "All",
    prompt_mode: str = "rag",
) -> str:
    if isinstance(context, list):
        context_text = "\n\n".join(context)
    else:
        context_text = str(context)

    scoped_calc_context = _compact_calc_context(calc_context, source)
    source_scope = _source_scope_text(source)

    if prompt_mode == "general_chat":
        return f"""
你是 CNC 進給系統選型助理，請一律用繁體中文回答。

使用者問題：
{question}

回答規則：
1. 這是一般對話，不要查詢或引用 RAG 知識庫。
2. 可以自然回覆；若使用者詢問你的能力，請簡短說明你能協助進給系統選型、規格資料查詢與計算結果解讀。
3. 不要編造目前未提供的規格、型號或計算結果。
4. 回答保持精簡、實用。
"""

    if prompt_mode == "calculation_qa":
        return f"""
你是 CNC 進給系統選型助理，請一律用繁體中文回答。

{source_scope}

目前計算結果：
- 使用者輸入條件：{scoped_calc_context.get("input_params")}
- 導程 mm：{scoped_calc_context.get("guide")}
- 動負荷 kgf：{scoped_calc_context.get("dynamic_load")}
- 系統需求扭矩 Nm：{scoped_calc_context.get("torque")}
- 安全驗證摘要：{scoped_calc_context.get("safety_summary")}
- 螺桿推薦摘要：{scoped_calc_context.get("recommendations_summary")}
- 慣量摘要：{scoped_calc_context.get("inertia_summary")}
- 馬達推薦摘要：{scoped_calc_context.get("motor_summary")}

使用者問題：
{question}

回答規則：
1. 這是計算結果問答，優先且主要根據「目前計算結果」回答。
2. 若來源範圍是 HIWIN 或 PMI，只能使用該品牌的螺桿推薦摘要；All 才能跨品牌比較。
3. 若計算結果缺少某項資料，請明確說明缺少資料，不要自行腦補。
4. 若回答馬達是否足夠，請比較系統需求扭矩與馬達最大扭矩，並檢查轉速資料。
5. 回答保持精簡、實用。
"""

    has_relevant_context = bool(context_text.strip())
    if not has_relevant_context:
        context_text = "知識庫未找到足夠相關資料。"

    if len(context_text) > MAX_CONTEXT_LENGTH:
        context_text = context_text[:MAX_CONTEXT_LENGTH] + "..."

    context_rule = (
        "參考資料已通過相關性門檻；回答不可超出目前計算結果與參考資料。"
        if has_relevant_context
        else "參考資料不足；只能根據目前計算結果回答可確認的部分，並明確說明知識庫未找到足夠相關資料。"
    )

    return f"""
你是 CNC 進給系統選型助理，請一律用繁體中文回答。

{source_scope}

目前計算結果：
- 導程 mm：{scoped_calc_context.get("guide")}
- 動負荷 kgf：{scoped_calc_context.get("dynamic_load")}
- 系統需求扭矩 Nm：{scoped_calc_context.get("torque")}
- 螺桿推薦摘要：{scoped_calc_context.get("recommendations_summary")}
- 馬達推薦摘要：{scoped_calc_context.get("motor_summary")}

使用者問題：
{question}

參考資料：
{context_text}

回答規則：
1. 優先根據「目前計算結果」回答。
2. {context_rule}
3. 若來源範圍是 HIWIN、PMI 或 FANUC，不得引用其他品牌來源資料；All 才能跨品牌比較。
4. 如果使用者問馬達是否符合需求，請比較需求扭矩與馬達最大扭矩，並檢查轉速。
5. 不得根據未通過相關性門檻的資料或常識自行腦補。
6. 若使用參考資料，請在答案末尾用簡短來源列出 Source/page/chunk。
7. 回答保持精簡、實用。
"""


def _json_for_prompt(value: Any) -> str:
    try:
        return json.dumps(value, ensure_ascii=False, indent=2, default=str)
    except Exception:
        return str(value)


def _source_scope_text(source: str) -> str:
    if source == "HIWIN":
        return (
            "資料範圍：HIWIN 只代表螺桿推薦品牌。"
            "馬達推薦仍固定來自 FANUC；不得使用 PMI 螺桿推薦。"
        )
    if source == "PMI":
        return (
            "資料範圍：PMI 只代表螺桿推薦品牌。"
            "馬達推薦仍固定來自 FANUC；不得使用 HIWIN 螺桿推薦。"
        )
    if source == "FANUC":
        return (
            "資料範圍：FANUC 只代表馬達推薦與馬達型錄。"
            "FANUC 不是螺桿品牌，不得輸出 FANUC 螺桿。"
        )
    return (
        "資料範圍：All 可使用 HIWIN 與 PMI 螺桿推薦，以及 FANUC 馬達推薦。"
        "HIWIN/PMI 是螺桿品牌；FANUC 是馬達品牌。"
    )


def _compact_calc_context(calc_context: dict[str, Any], source: str) -> dict[str, Any]:
    scoped = dict(calc_context or {})

    screw_recommendations = scoped.get("screw_recommendations")
    if not isinstance(screw_recommendations, dict):
        screw_recommendations = scoped.get("recommendations_summary")

    if isinstance(screw_recommendations, dict):
        if source in {"HIWIN", "PMI"}:
            filtered_screws = {source: screw_recommendations.get(source, [])}
        elif source == "FANUC":
            filtered_screws = {}
        else:
            filtered_screws = {
                brand: screw_recommendations.get(brand, [])
                for brand in ("HIWIN", "PMI")
                if brand in screw_recommendations
            }
        scoped["screw_recommendations"] = filtered_screws
        scoped["recommendations_summary"] = filtered_screws

    motor_recommendations = scoped.get("motor_recommendations")
    if not isinstance(motor_recommendations, dict):
        motor_recommendations = scoped.get("motor_summary")
    if isinstance(motor_recommendations, dict):
        scoped["motor_recommendations"] = {"FANUC": motor_recommendations.get("FANUC", [])}
        scoped["motor_summary"] = scoped["motor_recommendations"]

    return scoped


def _component_role_rules() -> str:
    return """
品牌與元件規則：
1. HIWIN、PMI 只能視為螺桿品牌，螺桿型號只能來自 screw_recommendations。
2. FANUC 只能視為馬達品牌，馬達型號只能來自 motor_recommendations。
3. 不得說「FANUC 螺桿」或把 FANUC 列在螺桿推薦中。
4. 不得把 αiS、αiF、βiS、βiF、γiS、γiF 這類馬達型號列為 HIWIN/PMI 螺桿型號。
5. 若指定 HIWIN 或 PMI，只能列該品牌的螺桿；FANUC 馬達仍可作為馬達推薦列出。
6. 若資料缺少，必須明確說明缺少，不可自行補品牌、型號或規格。
7. 型號、系列、品牌、單位與數值必須逐字複製 JSON 內容，不得翻譯、改寫或猜測。
欄位標籤規則：Maximum_Torque_Nm 是最大扭矩，Rated_Speed_RPM 是額定轉速，Rotor_Inertia_kgm2 是轉子慣量，matched_screw_spec 是對應螺桿組合。
""".strip()


def _recommendation_format_rules() -> str:
    return """
當問題要求推薦規格、目前推薦、列出推薦型號時，請優先使用以下格式：

螺桿推薦
- HIWIN 推薦型號規格：列出實際型號與可用規格欄位，例如系列、型號、外徑、導程、剛性。
- PMI 推薦型號規格：列出實際型號與可用規格欄位，例如系列、型號、外徑、導程、剛性。

馬達推薦
- FANUC 推薦型號規格：列出實際馬達型號、最大扭矩、額定轉速，並保留 matched_screw_spec。

若 source 或問題只指定單一品牌，僅列該品牌相關區塊；不要混入其他螺桿品牌。
不要照抄本段規則文字；必須讀取 JSON 內容後輸出實際資料值。
""".strip()


def optimize_prompt(
    question: str,
    context: list[str] | str,
    calc_context: dict[str, Any],
    source: str = "All",
    prompt_mode: str = "rag",
) -> str:
    if isinstance(context, list):
        context_text = "\n\n".join(context)
    else:
        context_text = str(context)

    scoped_calc_context = _compact_calc_context(calc_context, source)
    source_scope = _source_scope_text(source)
    component_rules = _component_role_rules()
    format_rules = _recommendation_format_rules()

    calc_payload = {
        "calculation_summary": scoped_calc_context.get("calculation_summary"),
        "input_params": scoped_calc_context.get("input_params"),
        "safety_summary": scoped_calc_context.get("safety_summary"),
        "inertia_summary": scoped_calc_context.get("inertia_summary"),
        "screw_recommendations": scoped_calc_context.get("screw_recommendations"),
        "motor_recommendations": scoped_calc_context.get("motor_recommendations"),
        "legacy_scalar_fields": {
            "guide_mm": scoped_calc_context.get("guide"),
            "dynamic_load_kgf": scoped_calc_context.get("dynamic_load"),
            "required_torque_nm": scoped_calc_context.get("torque"),
        },
    }
    calc_json = _json_for_prompt(calc_payload)

    if prompt_mode == "general_chat":
        return f"""
你是 CNC 進給系統技術助理。使用者目前不是在問技術規格或計算結果。

使用者問題：
{question}

回答規則：
1. 直接自然回覆，不要啟用 RAG 型錄資料。
2. 若使用者只是閒聊，簡短友善回答。
3. 不要捏造計算結果、品牌、型號或規格。
""".strip()

    if prompt_mode == "calculation_qa":
        return f"""
你是 CNC 進給系統技術助理，正在回答使用者對目前計算結果的問題。
{source_scope}

{component_rules}

計算結果資料（JSON）：
```json
{calc_json}
```

使用者問題：
{question}

回答格式要求：
{format_rules}

回答規則：
1. 只能根據上方 JSON 中的計算結果回答。
2. 螺桿推薦只從 screw_recommendations 取值；馬達推薦只從 motor_recommendations 取值。
3. 如果使用者問 HIWIN 所有推薦型號，只列 HIWIN 螺桿，不得列 FANUC 馬達。
4. 如果使用者問 PMI 所有推薦型號，只列 PMI 螺桿，不得列 HIWIN 或 FANUC 馬達。
5. 如果使用者問 FANUC 馬達推薦型號，只列 FANUC 馬達，不得列 HIWIN/PMI 螺桿為馬達。
6. 不要照抄欄位路徑、JSON key 或回答格式要求；請輸出 JSON 中的實際型號與數值。
7. 型號、系列、品牌、單位與數值必須逐字複製 JSON 內容，不得翻譯、改寫或猜測。
8. 如果資料不足，明確說明目前計算結果沒有提供該項資料，不要自行補完。
9. 回答使用繁體中文，保持簡潔。
""".strip()

    has_relevant_context = bool(context_text.strip())
    if not has_relevant_context:
        context_text = "知識庫未找到足夠相關資料。"

    if len(context_text) > MAX_CONTEXT_LENGTH:
        context_text = context_text[:MAX_CONTEXT_LENGTH] + "..."

    context_rule = (
        "只能使用通過 relevance gate 的型錄內容補充，不可加入未出現在 context 的型錄規格。"
        if has_relevant_context
        else "知識庫 context 不足時，只能依計算結果回答可確認資訊，並說明知識庫未找到足夠相關資料。"
    )

    return f"""
你是 CNC 進給系統技術助理。
{source_scope}

{component_rules}

目前計算結果（JSON）：
```json
{calc_json}
```

使用者問題：
{question}

通過 relevance gate 的知識庫內容：
{context_text}

回答格式要求：
{format_rules}

回答規則：
1. 優先根據目前計算結果回答。
2. {context_rule}
3. 螺桿型號只能來自 screw_recommendations 或明確相關的螺桿 context。
4. 馬達型號只能來自 motor_recommendations 或明確相關的 FANUC 馬達 context。
5. 不得把 FANUC 說成螺桿品牌，不得把 αiS/αiF 等馬達型號列為螺桿。
6. 不要照抄欄位路徑、JSON key 或回答格式要求；請輸出實際型號與數值。
7. 型號、系列、品牌、單位與數值必須逐字複製 JSON 內容，不得翻譯、改寫或猜測。
8. 若資訊不足，直接說明不足，不要腦補。
9. 回答使用繁體中文，保持簡潔；若引用型錄資料，可在末尾簡短列來源。
""".strip()


def query_ollama(
    question: str,
    context: list[str] | str,
    calc_context: dict[str, Any],
    model: str = DEFAULT_MODEL,
    timeout: int = 180,
    source: str = "All",
    prompt_mode: str = "rag",
) -> str:
    payload = {
        "model": model,
        "prompt": optimize_prompt(question, context, calc_context, source=source, prompt_mode=prompt_mode),
        "temperature": 0.1,
        "top_p": 0.9,
        "num_predict": 256,
        "repeat_penalty": 1.1,
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as exc:
        return f"Ollama is not available or failed to answer: {exc}"


def list_local_ollama_models(timeout: int = 5) -> list[str]:
    try:
        response = requests.get(OLLAMA_TAGS_URL, timeout=timeout)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return []

    models = []
    for item in data.get("models", []):
        name = item.get("name") or item.get("model")
        if name:
            models.append(str(name))

    return sorted(set(models), key=str.lower)


def model_display_name(model_name: str) -> str:
    if not model_name:
        return "No model selected"

    label = model_name
    if ":" in label:
        family, tag = label.split(":", 1)
        return f"{family} ({tag})"
    return label


def answer_question(
    question: str,
    source: str,
    calc_context: dict[str, Any],
    model: str = DEFAULT_MODEL,
) -> str:
    try:
        flow = _search_structured_flow(source, question, calc_context=calc_context)
    except Exception as exc:
        return f"RAG search failed: {exc}"

    if flow["route_decision"] in {"greeting", "test"}:
        return flow["route_answer"]
    if flow["route_decision"] == "general_chat":
        return query_ollama(question, [], {}, model=model, source=source, prompt_mode="general_chat")
    if flow["route_decision"] == "calculation_qa":
        return query_ollama(question, [], calc_context, model=model, source=source, prompt_mode="calculation_qa")

    return query_ollama(question, flow["final_context"], calc_context, model=model, source=source, prompt_mode="rag")


def trace_rag_flow(
    question: str,
    source: str,
    calc_context: dict[str, Any] | None = None,
    model: str = DEFAULT_MODEL,
    top_k: int = 3,
) -> dict[str, Any]:
    calc_context = calc_context or {}
    flow = _search_structured_flow(source, question, top_k=top_k, calc_context=calc_context)
    prompt_mode = flow["route_decision"] if flow["route_decision"] in {"general_chat", "calculation_qa"} else "rag"
    prompt = optimize_prompt(question, flow["final_context"], calc_context, source=source, prompt_mode=prompt_mode)
    return {
        "route_decision": flow["route_decision"],
        "search_mode": flow["search_mode"],
        "source_scope": source,
        "calc_context_keys": sorted(calc_context.keys()),
        "structured_query": flow["structured_query"],
        "top_k_raw_candidates": flow["top_k_raw_candidates"],
        "top_k_filtered_candidates": flow["top_k_filtered_candidates"],
        "final_context_preview": _preview("\n\n".join(flow["final_context"])),
        "prompt_preview": _preview(prompt),
        "prompt_mode": prompt_mode,
        "model": model,
    }
