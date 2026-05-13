"""Rebuild the Streamlit RAG ChromaDB collection from current Excel specs.

This script updates the collection used by:
code/04_applications/scripts/app_simple v3.py
"""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any

import chromadb
import pandas as pd
from chromadb.config import Settings


ROOT_DIR = Path(__file__).resolve().parents[3]
DB_PATH = ROOT_DIR / "databases" / "hiwin_vector_db"
COLLECTION_NAME = "screw_specs"

HIWIN_PATH = ROOT_DIR / "data" / "HIWIN_Final_Data_V1.xlsx"
PMI_PATH = ROOT_DIR / "data" / "PMI_Optimized_Core.xlsx"
FANUC_PATH = ROOT_DIR / "data" / "FANUC_Specs.xlsx"

OUTPUTS_DIR = ROOT_DIR / "code" / "outputs"
HIWIN_MANUAL_PATH = OUTPUTS_DIR / "HIWIN_final_chunks.json"
PMI_MANUAL_PATH = OUTPUTS_DIR / "PMI_final_chunks.json"
FANUC_MANUAL_PATH = OUTPUTS_DIR / "FANUC_final_chunks.json"

BATCH_SIZE = 100


def clean_value(value: Any) -> Any:
    """Convert pandas/numpy values into Chroma metadata-safe scalar values."""
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        value = value.item()
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def metadata_value(value: Any) -> str | int | float | bool:
    value = clean_value(value)
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def safe_id(value: Any) -> str:
    text = str(value).strip()
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"[^0-9A-Za-z_\-\u4e00-\u9fff\.]+", "_", text)
    return text.strip("_") or "unnamed"


def to_float(value: Any, default: float = 0.0) -> float:
    value = clean_value(value)
    if value in (None, ""):
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def add_original_columns(meta: dict[str, Any], row: pd.Series) -> dict[str, Any]:
    for key, value in row.to_dict().items():
        if key == "semantic_text":
            continue
        meta[str(key)] = metadata_value(value)
    return meta


def build_screw_records(path: Path, brand: str, source_file: str) -> list[dict[str, Any]]:
    df = pd.read_excel(path, sheet_name="Sheet1", engine="openpyxl").fillna("")
    required = ["型號", "公稱 外徑", "導程", "動負荷 C (kfg)", "靜負荷 Co (kfg)", "semantic_text"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"{path.name} missing required columns: {', '.join(missing)}")

    records: list[dict[str, Any]] = []
    for index, row in df.iterrows():
        model = str(row.get("型號", "")).strip() or f"unnamed_{index}"
        series = str(row.get("系列", "")).strip()
        document = str(row.get("semantic_text", "")).strip()
        if not document:
            document = (
                f"{brand} 滾珠螺桿型號 {model}，系列 {series}，"
                f"公稱外徑 {row.get('公稱 外徑', '')} mm，導程 {row.get('導程', '')} mm，"
                f"動負荷 {row.get('動負荷 C (kfg)', '')} kgf，"
                f"靜負荷 {row.get('靜負荷 Co (kfg)', '')} kgf。"
            )

        meta: dict[str, Any] = {
            "brand": brand,
            "category": "Screw",
            "data_type": "Specification",
            "source_file": source_file,
            "model_id": model,
            "series": series,
            "dia": to_float(row.get("公稱 外徑")),
            "lead": to_float(row.get("導程")),
            "dynamic_load_kgf": to_float(row.get("動負荷 C (kfg)")),
            "static_load_kgf": to_float(row.get("靜負荷 Co (kfg)")),
        }
        add_original_columns(meta, row)

        records.append(
            {
                "id": f"{brand.lower()}_s_{index}_{safe_id(model)}",
                "document": document,
                "metadata": meta,
            }
        )
    return records


def build_fanuc_model_records(path: Path) -> list[dict[str, Any]]:
    df = pd.read_excel(path, sheet_name="Model", engine="openpyxl").fillna("")
    required = ["Model", "Torque_Nm", "Max_RPM", "Inertia_kgm2"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"{path.name} Model sheet missing required columns: {', '.join(missing)}")

    records: list[dict[str, Any]] = []
    for index, row in df.iterrows():
        model = str(row.get("Model", "")).strip() or f"unnamed_{index}"
        torque = to_float(row.get("Torque_Nm"))
        max_rpm = to_float(row.get("Max_RPM"))
        inertia = to_float(row.get("Inertia_kgm2"))
        document = (
            f"FANUC 伺服馬達型號 {model}。"
            f"連續扭矩 {torque:g} N·m，最高轉速 {max_rpm:g} rpm，"
            f"馬達慣量 {inertia:g} kg·m²。"
        )
        meta: dict[str, Any] = {
            "brand": "FANUC",
            "category": "Motor",
            "data_type": "MotorModel",
            "source_file": path.name,
            "model_id": model,
            "torque_nm": torque,
            "max_rpm": max_rpm,
            "inertia_kgm2": inertia,
        }
        add_original_columns(meta, row)

        records.append(
            {
                "id": f"fanuc_model_{index}_{safe_id(model)}",
                "document": document,
                "metadata": meta,
            }
        )
    return records


def build_fanuc_detail_records(path: Path) -> list[dict[str, Any]]:
    df = pd.read_excel(path, sheet_name="ALL", engine="openpyxl").fillna("")
    required = ["Model", "Item", "Symbol", "Value", "Unit"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"{path.name} ALL sheet missing required columns: {', '.join(missing)}")

    records: list[dict[str, Any]] = []
    for index, row in df.iterrows():
        model = str(row.get("Model", "")).strip() or f"unnamed_{index}"
        item = str(row.get("Item", "")).strip()
        symbol = str(row.get("Symbol", "")).strip()
        value = metadata_value(row.get("Value"))
        unit = str(row.get("Unit", "")).strip()
        document = (
            f"FANUC 伺服馬達型號 {model} 的規格明細："
            f"{item}，符號 {symbol}，數值 {value} {unit}。"
        )
        meta: dict[str, Any] = {
            "brand": "FANUC",
            "category": "Motor",
            "data_type": "MotorDetail",
            "source_file": path.name,
            "model_id": model,
            "item": item,
            "symbol": symbol,
            "value": value,
            "unit": unit,
        }
        add_original_columns(meta, row)

        records.append(
            {
                "id": f"fanuc_detail_{index}_{safe_id(model)}_{safe_id(symbol or item)}",
                "document": document,
                "metadata": meta,
            }
        )
    return records


def build_manual_records(path: Path, brand: str, source_file: str) -> list[dict[str, Any]]:
    chunks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(chunks, list):
        raise ValueError(f"{path.name} must contain a JSON list of chunks.")

    records: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks):
        if not isinstance(chunk, dict):
            continue

        document = str(chunk.get("content", "")).strip()
        if not document:
            continue

        raw_meta = chunk.get("metadata")
        raw_meta = raw_meta if isinstance(raw_meta, dict) else {}
        page = chunk.get("page", chunk.get("source_page", raw_meta.get("page", raw_meta.get("source_page", ""))))
        manual_type = raw_meta.get("type", chunk.get("type", "technical_manual"))

        meta: dict[str, Any] = {
            "brand": brand,
            "category": "Manual",
            "data_type": "Manual",
            "source_file": source_file,
            "model_id": "",
            "page": metadata_value(page),
            "manual_type": metadata_value(manual_type),
        }

        for key, value in raw_meta.items():
            if key not in {"page", "source_page", "type"}:
                meta[str(key)] = metadata_value(value)

        records.append(
            {
                "id": f"{brand.lower()}_manual_{index}_{safe_id(page)}",
                "document": document,
                "metadata": meta,
            }
        )

    return records


def rebuild_collection(records: list[dict[str, Any]]) -> int:
    client = chromadb.PersistentClient(
        path=str(DB_PATH),
        settings=Settings(anonymized_telemetry=False),
    )

    existing = [
        collection if isinstance(collection, str) else collection.name
        for collection in client.list_collections()
    ]
    if COLLECTION_NAME in existing:
        client.delete_collection(COLLECTION_NAME)

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    for start in range(0, len(records), BATCH_SIZE):
        batch = records[start : start + BATCH_SIZE]
        collection.add(
            ids=[record["id"] for record in batch],
            documents=[record["document"] for record in batch],
            metadatas=[record["metadata"] for record in batch],
        )
        print(f"Added {min(start + BATCH_SIZE, len(records))}/{len(records)}")

    return collection.count()


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild ChromaDB screw_specs from Excel files.")
    parser.add_argument("--dry-run", action="store_true", help="Load and summarize records without writing ChromaDB.")
    args = parser.parse_args()

    records: list[dict[str, Any]] = []
    groups = [
        ("HIWIN", build_screw_records(HIWIN_PATH, "HIWIN", HIWIN_PATH.name)),
        ("PMI", build_screw_records(PMI_PATH, "PMI", PMI_PATH.name)),
        ("FANUC Model", build_fanuc_model_records(FANUC_PATH)),
        ("FANUC ALL", build_fanuc_detail_records(FANUC_PATH)),
        ("HIWIN Manual", build_manual_records(HIWIN_MANUAL_PATH, "HIWIN", HIWIN_MANUAL_PATH.name)),
        ("PMI Manual", build_manual_records(PMI_MANUAL_PATH, "PMI", PMI_MANUAL_PATH.name)),
        ("FANUC Manual", build_manual_records(FANUC_MANUAL_PATH, "FANUC", FANUC_MANUAL_PATH.name)),
    ]

    for name, group_records in groups:
        print(f"{name}: {len(group_records)} records")
        records.extend(group_records)

    print(f"Total records: {len(records)}")

    if args.dry_run:
        print("Dry run complete; ChromaDB was not modified.")
        return

    count = rebuild_collection(records)
    print(f"Rebuilt '{COLLECTION_NAME}' at {DB_PATH}")
    print(f"Collection count: {count}")


if __name__ == "__main__":
    main()
