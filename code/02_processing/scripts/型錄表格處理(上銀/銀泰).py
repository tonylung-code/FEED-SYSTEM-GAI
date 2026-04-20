"""
上銀表格處理

來源：code/上銀表格處裡.ipynb
將 notebook 中的文字擷取與表格清洗流程轉換成一般 Python 腳本。
"""

import fitz
import pdfplumber
import pandas as pd
import re


def step1_extract_text(pdf_path):
    """從 PDF 中提取文字，並進行初步的格式清理。"""
    try:
        doc = fitz.open(pdf_path)
        print(f"--- 檔案讀取成功：{pdf_path} ---")
        print(f"總頁數: {len(doc)}")

        extracted_data = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            raw_text = page.get_text("text")

            clean_text = re.sub(r'\n\s*\n', '\n\n', raw_text)
            clean_text = clean_text.strip()

            extracted_data.append({
                "page": page_num + 1,
                "content": clean_text
            })

            if page_num < 2:
                print(f"\n[第 {page_num + 1} 頁預覽]:")
                print(clean_text[:300] + "...")
                print("-" * 30)

        doc.close()
        return extracted_data
    except Exception as e:
        print(f"讀取失敗：{e}")
        return None


def clean_and_merge_table(df, series_name, page_num):
    if df is None or df.empty:
        return None

    df = df.replace('\n', '', regex=True)

    if len(df) > 2:
        new_columns = []
        for i in range(len(df.columns)):
            h1 = str(df.iloc[0, i]) if df.iloc[0, i] and df.iloc[0, i] != 'None' else ""
            h2 = str(df.iloc[1, i]) if df.iloc[1, i] and df.iloc[1, i] != 'None' else ""
            combined = f"{h1}{h2}".strip()
            if not combined:
                combined = f"Unnamed_{i}"
            new_columns.append(combined)

        final_cols = []
        counts = {}
        for col in new_columns:
            if col in counts:
                counts[col] += 1
                final_cols.append(f"{col}_{counts[col]}")
            else:
                counts[col] = 0
                final_cols.append(col)

        df.columns = final_cols
        df = df.iloc[2:].reset_index(drop=True)

    df.insert(0, "Series_Name", series_name)
    df.insert(1, "Source_Page", page_num)

    df = df[~df.iloc[:, 2].astype(str).str.contains(r'^[A-Za-z]$', na=False)]
    return df


def process_and_view(pdf_path, pages_to_process=None):
    all_processed_tables = []
    last_known_series = "Unknown"

    doc_fitz = fitz.open(pdf_path)
    with pdfplumber.open(pdf_path) as pdf_plumb:
        if pages_to_process is None:
            pages_to_process = range(len(pdf_plumb.pages))

        for i in pages_to_process:
            page_fitz = doc_fitz[i]
            words = page_fitz.get_text("words")
            words.sort(key=lambda w: (w[1] // 3, w[0]))
            full_sorted_text = "".join([w[4] for w in words])

            series_name = "Unknown"
            search_match = re.search(f"((?:F|R|PF|OF|DF)(?:SV|SW|DV|DW|SI|DI|SH|SC|DC))Type", full_sorted_text, re.IGNORECASE)
            if search_match:
                series_name = search_match.group(1)
            else:
                search_match = re.search(r"(?:F|R|PF|OF|DF)(?:SV|SW|DV|DW|SI|DI|SH|SC|DC)", full_sorted_text)
                if search_match:
                    series_name = search_match.group(0)

            if series_name == "Unknown":
                series_name = last_known_series
            else:
                last_known_series = series_name

            page_plumb = pdf_plumb.pages[i]
            table = page_plumb.extract_table({
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
                "snap_tolerance": 3,
                "join_tolerance": 2,
            })

            if table:
                raw_df = pd.DataFrame(table)
                clean_df = clean_and_merge_table(raw_df, series_name, i)

                if clean_df is not None:
                    all_processed_tables.append(clean_df)

    if all_processed_tables:
        return all_processed_tables

    print("未擷取到表格。")
    return None


def change_astype_robust(df, cols):
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df


def process_pmi_tables(pdf_path):
    """處理銀泰 (PMI) 型錄的表格擷取與清洗，類似 HIWIN 的方式先讀取文字判斷系列。"""
    table_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [],
        "explicit_horizontal_lines": [],
        "snap_tolerance": 3,
        "join_tolerance": 3,
    }

    all_processed_tables = []
    last_known_series = "Unknown"

    doc_fitz = fitz.open(pdf_path)
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            # --- 系列名擷取 (類似 HIWIN) ---
            page_fitz = doc_fitz[i]
            words = page_fitz.get_text("words")
            words.sort(key=lambda w: (w[1] // 3, w[0]))
            full_sorted_text = "".join([w[4] for w in words])

            series_name = "Unknown"
            # 調整正規表達式以匹配 PMI 系列，可能包含更多變體
            search_match = re.search(r"(F[A-Z]{2,3})", full_sorted_text)
            if search_match:
                series_name = search_match.group(1)
            else:
                # 備用：找其他可能的系列模式
                search_match = re.search(r"([A-Z]{3,4})", full_sorted_text)
                if search_match:
                    series_name = search_match.group(1)

            if series_name == "Unknown":
                series_name = last_known_series
            else:
                last_known_series = series_name

            # --- 表格擷取 ---
            tables = page.extract_tables(table_settings)
            
            for table in tables:
                df = pd.DataFrame(table)
                
                # 清洗邏輯
                df = df.dropna(how='all').dropna(axis=1, how='all')
                df = df.replace(r'\n', ' ', regex=True)
                
                if len(df) > 10:
                    mask = df.apply(lambda row: row.astype(str).str.contains("剛性|Q|油孔").any(), axis=1)
                    if mask.any():
                        header_idx = df[mask].index[-1]
                        df = df.iloc[header_idx + 1:].reset_index(drop=True).ffill()
                        a = df.iloc[:, :6]
                        b = df.iloc[:, -1]
                        df = pd.concat([a, b], axis=1)
                        
                        # 插入系列名
                        df.insert(0, "Series_Name", series_name)
                        df.insert(1, "Source_Page", i)
                        
                        # 排除標題殘影
                        df = df[~df.iloc[:, 2].astype(str).str.contains(r'^[A-Za-z]$', na=False)]
                        
                        all_processed_tables.append(df)
            
            print(f"第 {i+1} 頁處理完成 (系列: {series_name})")

    if all_processed_tables:
        return all_processed_tables
    else:
        print("沒抓到任何有效表格")
        return None


def build_final_pmi_df(all_processed_tables):
    """處理銀泰 (PMI) 的最終資料整理，類似 HIWIN。"""
    # 動態定義欄位名稱，根據實際欄位數調整
    base_col_name = [
        "系列", "sorce page", "型號", "公稱 外徑", "導程", "珠徑", "珠卷數", "動負荷 C (kfg)", "靜負荷 Co (kfg)", "剛性 kfg/umk"
    ]
    numeric_cols = [
        "公稱 外徑", "導程", "珠徑", "動負荷 C (kfg)", "靜負荷 Co (kfg)", "剛性 kfg/umk"
    ]

    processed_list = []
    for df_single in all_processed_tables:
        num_cols = len(df_single.columns)
        col_name = base_col_name[:num_cols]  # 根據實際欄位數截取
        temp_df = df_single.copy()
        temp_df.columns = col_name
        processed_list.append(temp_df)

    final_pmi = pd.concat(processed_list, ignore_index=True)

    # 移除標題殘影
    if "公稱 外徑" in final_pmi.columns:
        final_pmi = final_pmi[final_pmi["公稱 外徑"] != "公稱 外徑"].reset_index(drop=True)

    # 轉換資料型態
    available_numeric_cols = [col for col in numeric_cols if col in final_pmi.columns]
    final_pmi = change_astype_robust(final_pmi, available_numeric_cols)

    # 向下填充
    final_pmi = final_pmi.ffill()

    # 注入其他標籤
    final_pmi['brand'] = "PMI"
    final_pmi['category'] = "Screw"
    final_pmi['data_type'] = "Specification"

    # 格式化型號
    def format_model(row):
        try:
            dia = str(row.get("公稱 外徑", "")).strip()
            lead = str(row.get("導程", "")).strip()
            rigidity = str(row.get("剛性 kfg/umk", "")).strip()
            if dia == "" or "nan" in dia.lower() or "None" in dia:
                return "N/A"
            return f"{dia}-{lead}-{rigidity}"
        except:
            return "N/A"

    final_pmi['型號'] = final_pmi.apply(format_model, axis=1)
    final_pmi = final_pmi[final_pmi['型號'] != "N/A"].reset_index(drop=True)

    # 產生語意欄位
    def generate_pmi_semantic(row):
        return (
            f"這是銀泰 (PMI) 的滾珠螺桿規格。系列名稱為 {row.get('系列', 'Unknown')}，"
            f"完整型號為 {row.get('型號', 'N/A')}。其主要參數如下：公稱外徑為 {row.get('公稱 外徑', 'N/A')} mm，"
            f"導程為 {row.get('導程', 'N/A')} mm，珠徑為 {row.get('珠徑', 'N/A')} mm，珠卷數為 {row.get('珠卷數', 'N/A')}。"
            f"在性能指標方面，其動負荷 (Ca) 為 {row.get('動負荷 C (kfg)', 'N/A')} kgf，"
            f"靜負荷 (Co) 為 {row.get('靜負荷 Co (kfg)', 'N/A')} kgf，剛性為 {row.get('剛性 kfg/umk', 'N/A')} kgf/umk。"
        )

    final_pmi['semantic_text'] = final_pmi.apply(generate_pmi_semantic, axis=1)

    return final_pmi


def generate_semantic(row):
    return (
        f"這是上銀 (HIWIN) 的滾珠螺桿規格。系列名稱為 {row['系列']}，"
        f"完整型號為 {row['型號']}。其主要參數如下：公稱外徑為 {row['公稱 外徑']} mm，"
        f"導程為 {row['導程']} mm，珠徑為 {row['珠徑']} mm，珠卷數為 {row['珠卷數']}。"
        f"在性能指標方面，其動負荷 (Ca) 為 {row['動負荷 C (kfg)']} kgf，"
        f"靜負荷 (Co) 為 {row['靜負荷 Co (kfg)']} kgf，剛性為 {row['剛性 kfg/umk']} kgf/umk。"
    )


def build_final_hiwin_df(final_hiwin_df):
    col_name = [
        "系列", "sorce page", "型號", "公稱 外徑", "導程", "珠徑", "PCD", "根徑",
        "珠卷數", "剛性 kfg/umk", "動負荷 C (kfg)", "靜負荷 Co (kfg)"
    ]
    numeric_cols = [
        "公稱 外徑", "導程", "珠徑", "PCD", "根徑",
        "剛性 kfg/umk", "動負荷 C (kfg)", "靜負荷 Co (kfg)"
    ]

    processed_list = []
    for df_single in final_hiwin_df:
        temp_df = df_single.iloc[:, :12].copy()
        temp_df.columns = col_name
        processed_list.append(temp_df)

    final_hiwin = pd.concat(processed_list, ignore_index=True)
    final_hiwin = final_hiwin[final_hiwin["公稱 外徑"] != "公稱 外徑"].reset_index(drop=True)
    final_hiwin = change_astype_robust(final_hiwin, numeric_cols)
    final_hiwin = final_hiwin.ffill()
    final_hiwin['semantic_text'] = final_hiwin.apply(generate_semantic, axis=1)
    return final_hiwin


if __name__ == '__main__':
    # 預設使用銀泰 (PMI) 型錄，可根據需要修改路徑
    pdf_path = r"C:\Users\e11338\Desktop\銀泰目錄分割\銀泰螺桿型錄 切割 共67頁.pdf"

    # 判斷品牌
    if "PMI" in pdf_path.upper() or "銀泰" in pdf_path:
        brand = "PMI"
        print("開始處理銀泰 (PMI) 表格...\n")
        all_processed_tables = process_pmi_tables(pdf_path)
        if all_processed_tables:
            final_df = build_final_pmi_df(all_processed_tables)
            output_file = "PMI_Final_Data_V3.xlsx"
        else:
            final_df = None
    else:
        brand = "HIWIN"
        print("開始處理上銀 (HIWIN) 表格...\n")
        final_hiwin_df = process_and_view(pdf_path)
        if final_hiwin_df:
            final_df = build_final_hiwin_df(final_hiwin_df)
            output_file = "HIWIN_Final_Data_V1.xlsx"
        else:
            final_df = None

    if final_df is not None:
        final_df.to_excel(output_file, index=False)
        print("資料清洗完成！")
        print(f"已輸出：{output_file}")
        print(final_df.head(30))
    else:
        print("沒有可處理的表格。")
