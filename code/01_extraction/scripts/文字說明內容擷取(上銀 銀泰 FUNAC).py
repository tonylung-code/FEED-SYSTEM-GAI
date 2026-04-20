"""
文字說明內容擷取(上銀 銀泰 FUNAC)

目標：從上銀、銀泰、馬達型錄中擷取「文字說明內容」和「計算公式」，
並過濾掉表格噪音、無意義符號與純數據，讓後續 RAG 更乾淨更高效。
"""

import fitz
import re
import os
import pandas as pd
import unicodedata
from datetime import datetime

CATALOGS = {
    "FANUC": r"C:\Users\e11338\Desktop\Feed System GAI\data\B65542EN_01_ai-D伺服馬達仕樣.pdf",
    "HIWIN": r"C:\Users\e11338\Desktop\Feed System GAI\data\上銀滾珠螺桿.pdf",
    "PMI": r"C:\Users\e11338\Desktop\Feed System GAI\data\銀泰螺桿型錄.pdf",
}

OUTPUT_BASE = "catalog_text_formula_extraction"

# --- 清理函式 ---

def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = text.replace('\u3000', ' ')
    text = re.sub(r'\u00A0', ' ', text)
    text = re.sub(r'[\u200b-\u200f\u2028\u2029]', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    return text.strip()


def digit_ratio(text: str) -> float:
    if not text:
        return 0.0
    total = len(text)
    digits = len(re.findall(r'[0-9０-９\-\./××±%]', text))
    return digits / total if total else 0.0


def page_text_stats(text: str, page) -> dict:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    total_chars = len(text)
    digits = len(re.findall(r'[0-9０-９\-\./×±%]', text))
    digit_ratio_all = digits / total_chars if total_chars else 0.0

    numeric_lines = [line for line in lines if digit_ratio(line) > 0.65 and len(re.sub(r'\s+', '', line)) > 10]
    punctuation_lines = [line for line in lines if re.search(r'[。．，,，:；;！?!]', line)]
    table_markers = sum(1 for line in lines if re.search(r'[\|\+\-]{3,}|\bPage\b|\b頁\b|\bTable\b|\b表格\b', line))
    data_lines = [line for line in lines if re.search(r'\d', line) and not re.search(r'[。．，,，:；;！?!]', line)]
    image_count = len(page.get_images(full=True)) if hasattr(page, 'get_images') else 0

    return {
        'line_count': len(lines),
        'numeric_line_ratio': len(numeric_lines) / len(lines) if lines else 0.0,
        'punctuation_line_ratio': len(punctuation_lines) / len(lines) if lines else 0.0,
        'table_marker_ratio': table_markers / len(lines) if lines else 0.0,
        'data_line_ratio': len(data_lines) / len(lines) if lines else 0.0,
        'digit_ratio': digit_ratio_all,
        'image_count': image_count,
    }


def is_table_heavy_page(text: str, page) -> bool:
    stats = page_text_stats(text, page)
    # 進一步放寬條件，避免跳過有公式的頁面
    if stats['image_count'] > 3 and stats['numeric_line_ratio'] > 0.4:
        return True
    if stats['numeric_line_ratio'] > 0.7:
        return True
    if stats['data_line_ratio'] > 0.7 and stats['punctuation_line_ratio'] < 0.05:
        return True
    if stats['table_marker_ratio'] > 0.4:
        return True
    if stats['digit_ratio'] > 0.5 and stats['punctuation_line_ratio'] < 0.05:
        return True
    # 新增：如果data_lines比例很高，即使有標點，也可能是表格
    if stats['data_line_ratio'] > 0.8:
        return True
    # 新增：如果行數很多且data_lines比例中等高，也可能是表格
    if stats['line_count'] > 200 and stats['data_line_ratio'] > 0.4:
        return True
    # 新增：如果行數很多且數字比例中等，也可能是表格
    if stats['line_count'] > 300 and stats['digit_ratio'] > 0.04:
        return True
    return False


def page_has_formula_context(text: str) -> bool:
    # 放寬公式上下文判斷
    return bool(re.search(r'公式|計算式|計算|式\b|Formula|Calculation|sqrt|sin|cos|tan|log|ln|exp|pow|=|≤|≥|±|×|÷|Equation', text, re.I))


def page_has_description_context(text: str) -> bool:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        return False
    # 放寬說明上下文，包含英文標點
    punctuation_ratio = sum(1 for line in lines if re.search(r'[。．，,，:；;！?!.?!:;]', line)) / len(lines)
    return punctuation_ratio > 0.1 or bool(re.search(r'說明|特性|性能|用途|優勢|适用|注意|Description|Specification|Feature|Note', text, re.I))


def is_formula_line(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    formula_symbols = re.search(r'[=＝±×＊\*/\^√Δπθαβγ]|\b(sin|cos|tan|log|ln|exp|sqrt|pow)\b', line, re.I)
    has_digits = bool(re.search(r'\d', line))
    has_letters = bool(re.search(r'[A-Za-zα-ωΑ-Ω]', line))
    if formula_symbols and has_digits:
        return True
    if re.search(r'\b[A-Za-z]\w*\s*[:=]', line) and has_digits:
        return True
    if re.search(r'\bK\d+\b', line) and has_digits:
        return True
    return False


def is_model_block(block: str) -> bool:
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    if not lines:
        return False

    model_like = 0
    for line in lines:
        if re.search(r'\b[A-Z]{1,5}\d{1,3}[\-\/]?\d*[A-Z0-9]*\b', line) and len(line) < 80:
            model_like += 1
    return model_like / max(1, len(lines)) > 0.6


def is_table_like_block(block: str) -> bool:
    if not block or len(block) < 30:
        return False
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    numeric_lines = [line for line in lines if digit_ratio(line) > 0.55 and len(re.sub(r'\s+', '', line)) > 10]
    if lines and len(numeric_lines) / len(lines) > 0.4:
        return True

    tokens = re.split(r'\s+', block)
    numeric_tokens = sum(1 for token in tokens if re.fullmatch(r'[\d\.\-±×＊\*/%\(\)]+', token) or (re.search(r'\d', token) and not re.search(r'[\u4e00-\u9fffA-Za-z]', token)))
    if len(tokens) > 12 and numeric_tokens / len(tokens) > 0.45 and not re.search(r'[。．，,，:；;！?!]', block):
        return True

    if re.search(r'\b[A-Z0-9]{2,6}-\d+\b', block) and digit_ratio(block) > 0.35 and not re.search(r'[。．，,，:；;！?!]', block):
        return True

    return False


def is_description_block(block: str) -> bool:
    if not block or len(block) < 20:
        return False
    chinese = bool(re.search(r'[\u4e00-\u9fff]', block))
    english = bool(re.search(r'[A-Za-z]{2,}', block))
    punctuation = bool(re.search(r'[。．，,，:；;！?!]', block))
    if chinese and punctuation:
        return True
    if english and len(block) > 40 and digit_ratio(block) < 0.7:
        return True
    if chinese and len(block) > 40 and digit_ratio(block) < 0.8:
        return True
    return False


def clean_block_text(block: str) -> str:
    block = normalize_text(block)
    block = re.sub(r'Page\s*\d+(/\d+)?', '', block, flags=re.I)
    block = re.sub(r'第\s*\d+\s*頁', '', block)
    block = re.sub(r'\b(?:Table|表格|圖|Figure)\b', '', block)
    block = re.sub(r'\-\s*\n\s*', '', block)
    block = re.sub(r'\n{2,}', '\n', block)

    lines = [line.strip() for line in block.split('\n') if line.strip()]
    merged_lines = []
    for line in lines:
        if merged_lines:
            prev = merged_lines[-1]
            if not re.search(r'[。．！!?\.:]$', prev) and not prev.endswith(')') and not is_formula_line(line) and not re.match(r'^[\-•\u2022\*]', line):
                merged_lines[-1] = prev + ' ' + line
            else:
                merged_lines.append(line)
        else:
            merged_lines.append(line)

    block = '\n'.join(merged_lines)
    block = re.sub(r'\s{2,}', ' ', block)
    block = re.sub(r'^[\-•\u2022\*]+\s*', '', block, flags=re.MULTILINE)
    block = block.strip()
    return block


def split_into_blocks(text: str) -> list[str]:
    blocks = []
    paragraphs = re.split(r'\n\s*\n', text)
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if len(paragraph) > 500:
            lines = [line.strip() for line in paragraph.split('\n') if line.strip()]
            buffer = []
            for line in lines:
                buffer.append(line)
                if re.search(r'[。．！!?]$', line) and len(buffer) > 0:
                    blocks.append(' '.join(buffer))
                    buffer = []
            if buffer:
                blocks.append(' '.join(buffer))
        else:
            blocks.append(paragraph)
    return blocks


def is_formula_block(block: str) -> bool:
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    formula_lines = sum(1 for line in lines if is_formula_line(line))
    if formula_lines / max(1, len(lines)) > 0.25:
        return True
    if re.search(r'公式|計算式|計算|公式為|公式：|Formula|Calculation', block, re.I):
        return True
    return False


def classify_block(block: str) -> str:
    if is_table_like_block(block) or is_model_block(block):
        return 'other'
    if is_formula_block(block):
        return 'formula'
    if is_description_block(block):
        return 'description'
    return 'other'


def extract_page_blocks(page_text: str, page_category: str) -> list[dict]:
    # 移除分類，只保留所有非表格的區塊
    blocks = split_into_blocks(page_text)
    extracted = []
    for block in blocks:
        cleaned = clean_block_text(block)
        if not cleaned:
            continue
        # 簡單過濾明顯的表格區塊
        if is_table_like_block(cleaned) or is_model_block(cleaned):
            continue
        extracted.append(cleaned)

    # 合併chunks到適當長度 (300-1000字元)
    merged = []
    current = ""
    for block in extracted:
        if len(current) + len(block) < 300:
            current += block + "\n\n"
        elif len(current) + len(block) <= 1000:
            current += block + "\n\n"
            merged.append(current.strip())
            current = ""
        else:
            if current:
                merged.append(current.strip())
            current = block + "\n\n"
    if current:
        merged.append(current.strip())

    return [{'content': chunk} for chunk in merged if chunk]


def extract_catalog_text(pdf_path: str, catalog_name: str) -> list[dict]:
    if not os.path.exists(pdf_path):
        print(f'找不到檔案: {pdf_path}')
        return []

    print(f'開始處理 {catalog_name}: {pdf_path}')
    doc = fitz.open(pdf_path)
    results = []
    for page_index in range(doc.page_count):
        page = doc[page_index]
        raw_text = page.get_text('text') or ''
        page_text = normalize_text(raw_text)
        if not page_text:
            continue

        page_category = 'table_heavy' if is_table_heavy_page(page_text, page) else 'text_heavy'
        if page_category == 'table_heavy':
            continue  # 直接跳過表格頁面，不進行段落判斷
        blocks = extract_page_blocks(page_text, page_category)
        for block in blocks:
            results.append({
                'catalog': catalog_name,
                'pdf_path': pdf_path,
                'page': page_index + 1,
                'page_category': page_category,
                'content': block['content'],
            })
    doc.close()
    return results


def save_results(results: list[dict], timestamp: str) -> None:
    if not results:
        print('沒有擷取到任何內容。')
        return

    df = pd.DataFrame(results)
    excel_path = f'{OUTPUT_BASE}_{timestamp}.xlsx'
    json_path = f'{OUTPUT_BASE}_{timestamp}.json'
    md_path = f'{OUTPUT_BASE}_{timestamp}.md'

    df.to_excel(excel_path, index=False)
    df.to_json(json_path, force_ascii=False, orient='records', indent=2)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f'# 文字說明與公式擷取結果 ({timestamp})\n\n')
        for idx, row in df.iterrows():
            f.write(f'## {row.catalog} - 第 {row.page} 頁\n')
            f.write(f'- page_category: {row.page_category}\n')
            f.write(f'- source: {os.path.basename(row.pdf_path)}\n\n')
            f.write(row.content + '\n\n')
            f.write('---\n\n')

    print(f'已輸出: {excel_path}, {json_path}, {md_path}')


def run_all():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results = []
    for catalog_name, pdf_path in CATALOGS.items():
        results.extend(extract_catalog_text(pdf_path, catalog_name))
    save_results(results, timestamp)


if __name__ == '__main__':
    run_all()
