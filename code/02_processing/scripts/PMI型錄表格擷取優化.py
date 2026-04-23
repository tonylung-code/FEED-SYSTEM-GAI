"""
PMI 型錄表格擷取優化版

輸出欄位：
- Series_Name
- Source_Page
- 型號
- 外徑
- 導程
- 鋼珠直徑
- 循環圈數
- 動負荷
- 靜負荷
- 剛性
- semantic_text
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd
import pdfplumber


TABLE_SETTINGS = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "lines",
    "explicit_vertical_lines": [],
    "explicit_horizontal_lines": [],
    "snap_tolerance": 3,
    "join_tolerance": 3,
}

OUTPUT_COLUMNS = [
    "Series_Name",
    "Source_Page",
    "型號",
    "外徑",
    "導程",
    "鋼珠直徑",
    "循環圈數",
    "動負荷",
    "靜負荷",
    "剛性",
    "semantic_text",
]

HEADER_MARKERS = re.compile(
    r"型號|BALLSCREW|單位:mm|外徑|導程|鋼珠|尺寸|循環|Cam|Coam|動負荷|靜負荷|kgf|油孔|螺絲孔",
    re.IGNORECASE,
)


def normalize_cell(value: object) -> str:
    if value is None:
        return ""
    text = str(value).replace("\n", " ").replace("\r", " ").strip()
    text = re.sub(r"\s+", " ", text)
    if text.lower() in {"nan", "none"}:
        return ""
    return text


def parse_number(value: object) -> float | None:
    text = normalize_cell(value)
    if not text:
        return None
    text = text.replace(",", "")
    if re.fullmatch(r"-?\d+(?:\.\d+)?", text):
        return float(text)
    return None


def format_number(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "N/A"
    if float(value).is_integer():
        return str(int(value))
    return f"{value:g}"


def extract_series_name(page: pdfplumber.page.Page, last_series: str = "Unknown") -> str:
    text = page.extract_text() or ""
    # PMI 系列在頁面中常見形式如 FSIC / FSDC / FDIC / RDIC
    match = re.search(r"\b((?:F|R|O|D)[A-Z]{2,4}C)\b", text)
    if match:
        return match.group(1)
    return last_series


def looks_like_main_table(df: pd.DataFrame) -> bool:
    if df.shape[0] < 6 or df.shape[1] < 7:
        return False
    header_text = " ".join(normalize_cell(v) for v in df.head(2).to_numpy().flatten())
    return bool(re.search(r"導程|Cam|Coam|鋼珠|剛性", header_text, re.IGNORECASE))


def is_candidate_row(row: list[str]) -> bool:
    text = " ".join(row)
    if not text.strip():
        return False
    if HEADER_MARKERS.search(text):
        return False
    if not normalize_cell(row[3] if len(row) > 3 else None):
        return False
    if parse_number(row[4] if len(row) > 4 else None) is None:
        return False
    if parse_number(row[5] if len(row) > 5 else None) is None:
        return False
    if parse_number(row[-1]) is None:
        return False
    return True


def build_model(series_name: str, diameter: float | None, lead: float | None) -> str:
    return f"{series_name}-{format_number(diameter)}-{format_number(lead)}"


def build_semantic_text(row: pd.Series) -> str:
    return (
        f"這是銀泰 (PMI) 的滾珠螺桿規格。系列名稱為 {row['Series_Name']}，"
        f"型號為 {row['型號']}。外徑為 {format_number(row['外徑'])} mm，"
        f"導程為 {format_number(row['導程'])} mm，鋼珠直徑為 {format_number(row['鋼珠直徑'])} mm，"
        f"循環圈數為 {row['循環圈數']}，"
        f"動負荷為 {format_number(row['動負荷'])} kgf，靜負荷為 {format_number(row['靜負荷'])} kgf，"
        f"剛性為 {format_number(row['剛性'])} kgf/um。"
    )


def finalize_model_id(row: pd.Series) -> str:
    return (
        f"{row['Series_Name']}-{format_number(row['外徑'])}-{format_number(row['導程'])}"
        f"-BD{format_number(row['鋼珠直徑'])}-C{row['循環圈數']}"
    )


def process_main_table(df: pd.DataFrame, series_name: str, page_num: int) -> pd.DataFrame | None:
    rows = [[normalize_cell(v) for v in row] for row in df.to_numpy().tolist()]

    extracted: list[dict[str, object]] = []
    current_diameter: float | None = None
    current_lead: float | None = None
    current_ball_diameter: float | None = None
    current_cycle_count: str | None = None

    for row in rows[2:]:
        if not is_candidate_row(row):
            continue

        diameter = parse_number(row[0])
        lead = parse_number(row[1])
        ball_diameter = parse_number(row[2])
        cycle_count = normalize_cell(row[3])
        dynamic_load = parse_number(row[4])
        static_load = parse_number(row[5])
        rigidity = parse_number(row[-1])

        if diameter is not None:
            current_diameter = diameter
        if lead is not None:
            current_lead = lead
        if ball_diameter is not None:
            current_ball_diameter = ball_diameter
        if cycle_count:
            current_cycle_count = cycle_count

        # 同一外徑群組的續列通常省略外徑或鋼珠直徑
        diameter = current_diameter
        lead = current_lead
        ball_diameter = current_ball_diameter
        cycle_count = current_cycle_count

        if None in (diameter, lead, ball_diameter, dynamic_load, static_load, rigidity) or not cycle_count:
            continue

        record = {
            "Series_Name": series_name,
            "Source_Page": page_num,
            "型號": build_model(series_name, diameter, lead),
            "外徑": diameter,
            "導程": lead,
            "鋼珠直徑": ball_diameter,
            "循環圈數": cycle_count,
            "動負荷": dynamic_load,
            "靜負荷": static_load,
            "剛性": rigidity,
        }
        extracted.append(record)

    if not extracted:
        return None

    result = pd.DataFrame(extracted)
    result = result.drop_duplicates(
        subset=["Series_Name", "Source_Page", "外徑", "導程", "鋼珠直徑", "循環圈數", "動負荷", "靜負荷", "剛性"]
    )
    return result.reset_index(drop=True)


def extract_pmi_tables(pdf_path: str | Path) -> tuple[pd.DataFrame | None, list[int]]:
    all_rows: list[pd.DataFrame] = []
    empty_pages: list[int] = []
    last_series = "Unknown"

    with pdfplumber.open(str(pdf_path)) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            series_name = extract_series_name(page, last_series)
            last_series = series_name

            tables = page.extract_tables(TABLE_SETTINGS) or []
            page_results: list[pd.DataFrame] = []

            for table in tables:
                raw_df = pd.DataFrame(table).dropna(how="all").dropna(axis=1, how="all")
                if raw_df.empty or not looks_like_main_table(raw_df):
                    continue
                processed = process_main_table(raw_df, series_name, page_num)
                if processed is not None and not processed.empty:
                    page_results.append(processed)

            if page_results:
                merged = pd.concat(page_results, ignore_index=True)
                all_rows.append(merged)
                print(f"第 {page_num} 頁處理完成，系列={series_name}，擷取列數={len(merged)}")
            else:
                empty_pages.append(page_num)
                print(f"第 {page_num} 頁未擷取到有效表格，系列={series_name}")

    if not all_rows:
        return None, empty_pages

    final_df = pd.concat(all_rows, ignore_index=True)
    final_df = final_df.drop_duplicates(
        subset=["Series_Name", "Source_Page", "外徑", "導程", "鋼珠直徑", "循環圈數", "動負荷", "靜負荷", "剛性"]
    )
    final_df = final_df.sort_values(["Source_Page", "Series_Name", "外徑", "導程"]).reset_index(drop=True)
    final_df["型號"] = final_df.apply(finalize_model_id, axis=1)
    final_df["semantic_text"] = final_df.apply(build_semantic_text, axis=1)
    final_df = final_df[OUTPUT_COLUMNS]
    return final_df, empty_pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PMI 型錄表格擷取優化版")
    parser.add_argument(
        "--pdf",
        default="/Users/tonylung/Downloads/銀泰螺桿型錄 切割 共67頁.pdf",
        help="PMI PDF 路徑",
    )
    parser.add_argument(
        "--output",
        default="outputs/PMI_Optimized_Core.xlsx",
        help="輸出 Excel 路徑",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = Path(args.pdf)
    output_path = Path(args.output)

    if not pdf_path.exists():
        raise FileNotFoundError(f"找不到 PDF：{pdf_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    final_df, empty_pages = extract_pmi_tables(pdf_path)
    if final_df is None or final_df.empty:
        print("沒有擷取到任何有效資料。")
        return

    final_df.to_excel(output_path, index=False)

    print("\n擷取完成")
    print(f"總列數：{len(final_df)}")
    print(f"輸出檔案：{output_path}")
    print("\n前 10 筆樣本：")
    print(final_df.head(10).to_string(index=False))
    if empty_pages:
        print(f"\n未擷取到有效表格的頁碼：{empty_pages}")


if __name__ == "__main__":
    main()
