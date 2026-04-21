"""
PMI Catalog Processing Script

Fixed version without fitz dependency.
"""

import pdfplumber
import pandas as pd
import re
import os
from pathlib import Path


def step1_extract_text(pdf_path):
    """從 PDF 中提取文字，並進行初步的格式清理。"""
    try:
        extracted_data = []
        with pdfplumber.open(pdf_path) as pdf:
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                raw_text = page.extract_text()
                if raw_text:
                    clean_text = re.sub(r'\n\s*\n', '\n\n', raw_text)
                    clean_text = clean_text.strip()
                else:
                    clean_text = ""

                extracted_data.append({
                    "page": page_num + 1,
                    "content": clean_text
                })

                if page_num < 2:
                    print(f"\n[第 {page_num + 1} 頁預覽]:")
                    print(clean_text[:300] + "...")
                    print("-" * 30)

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

    with pdfplumber.open(pdf_path) as pdf_plumb:
        if pages_to_process is None:
            pages_to_process = range(len(pdf_plumb.pages))

        for i in pages_to_process:
            page_fitz = pdf_plumb.pages[i]
            words = page_fitz.extract_words()
            words.sort(key=lambda w: (w['top'] // 3, w['x0']))
            full_sorted_text = "".join([w['text'] for w in words])

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
    """轉換指定列為數值型態，忽略不存在的列"""
    for c in cols:
        if c in df.columns:
            try:
                # 確保是 Series 後再進行轉換
                series = df[c]
                if isinstance(series, pd.Series):
                    df[c] = pd.to_numeric(series, errors='coerce')
                else:
                    print(f"警告：列 '{c}' 不是 Series，跳過轉換")
            except Exception as e:
                print(f"警告：無法轉換列 '{c}'：{e}")
        else:
            print(f"警告：列 '{c}' 不存在於 DataFrame 中")
    return df


def process_pmi_tables(pdf_path):
    """
    處理銀泰 (PMI) 型錄的表格擷取與清洗。
    
    改進：
    - 動態錨定表頭（而非硬切位置）
    - 自動補上未命名欄位
    - 刪除表頭之前的雜訊列
    """
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

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            # --- 系列名擷取 ---
            page_fitz = page  # Use pdfplumber page
            words = page.extract_words()  # Extract words as list of dicts
            words_sorted = sorted(words, key=lambda w: (w['top'] // 3, w['x0']))
            full_sorted_text = "".join([w['text'] for w in words_sorted])

            series_name = "Unknown"
            search_match = re.search(r"(F[A-Z]{2,3})", full_sorted_text)
            if search_match:
                series_name = search_match.group(1)
            else:
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
                df = df.replace(r'\n', ' ', regex=True).replace(r'\r', ' ', regex=True)
                
                if len(df) > 10:
                    # --- 動態表頭錨定 ---
                    # 尋找包含特定關鍵詞的列作為表頭
                    header_keywords = r"型號|外徑|導程|動負荷|靜負荷|Ca|Co|剛性|型号|外径|导程|动|静|TYPE|Dg6|Lead|Load|Rigidity"
                    header_idx = -1
                    
                    for idx, row in df.iterrows():
                        row_text = ' '.join([str(x) for x in row])
                        if re.search(header_keywords, row_text):
                            # 檢查下一行是否有數值
                            if idx + 1 < len(df):
                                next_row = df.iloc[idx + 1]
                                numeric_count = sum(pd.to_numeric(next_row, errors='coerce').notna())
                                if numeric_count > 2:  # 如果下一行有超過2個數值，則這是頭部
                                    header_idx = idx
                                    break
                            else:
                                header_idx = idx
                                break
                    
                    if header_idx == -1:
                        # 備用：尋找含有數字密度高的列
                        numeric_counts = df.apply(lambda row: sum(pd.to_numeric(row, errors='coerce').notna()), axis=1)
                        if numeric_counts.max() > 2:
                            header_idx = numeric_counts.idxmax()
                            print(f"⚠️  Page {i+1}: Header fallback to row {header_idx} (numeric density)")
                        else:
                            print(f"⚠️  Page {i+1}: No valid header found, skipping table")
                            continue
                    
                    # 提取表頭列，清理空白
                    header_row = df.iloc[header_idx].copy()
                    print(f"Debug: Page {i+1} header row {header_idx}: {header_row.tolist()}")
                    new_columns = []
                    for col_idx, cell in enumerate(header_row):
                        cell_str = str(cell).strip() if cell and str(cell) != 'None' else ""
                        if not cell_str:
                            cell_str = f"未命名_{col_idx}"
                        new_columns.append(cell_str)
                    
                    # 處理重複欄位名
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
                    
                    # 刪除表頭（含）以上的雜訊列，只保留純數據
                    df = df.iloc[header_idx + 1:].reset_index(drop=True).ffill()
                    print(f"Debug: Page {i+1} first data row: {df.iloc[0].tolist() if not df.empty else 'empty'}")
                    
                    # 插入系列名和頁碼
                    df.insert(0, "Series_Name", series_name)
                    df.insert(1, "Source_Page", i)
                    
                    # 排除標題殘影（過濾掉型號欄位中只有單個英文字母的列）
                    if len(df.columns) > 2:
                        df = df[~df.iloc[:, 2].astype(str).str.contains(r'^[A-Za-z]$', na=False)]
                    
                    if not df.empty:
                        all_processed_tables.append(df)
            
            print(f"第 {i+1} 頁處理完成 (系列: {series_name})")

    if all_processed_tables:
        return all_processed_tables
    else:
        print("沒抓到任何有效表格")
        return None


def build_final_pmi_df(all_processed_tables):
    """
    處理銀泰 (PMI) 的最終資料整理。
    
    改進：
    - 使用 pd.concat 自動對齊不同欄位數的表格
    - 模糊字典映射進行欄位標準化
    - 過濾重複欄位，補上缺失標準欄位
    - 保留原有優秀邏輯（型態轉換、ffill、語意生成）
    """
    # 首先直接 concat，讓 Pandas 自動對齊
    final_pmi = pd.concat(all_processed_tables, ignore_index=True, sort=False)
    
    # --- 模糊字典映射 --- 
    rename_dict = {}
    
    # 定義標準欄位對應規則
    mapping_rules = {
        "型號": r"型號|型号|model|MODEL|Code|TYPE|型 號",
        "公稱 外徑": r"外徑|外径|直径|nominal|d(?:\s|_|$|mm)|Dg6|D6",
        "導程": r"導程|导程|lead|l(?:\s|_|$|mm)|導 程",
        "珠徑": r"珠徑|珠径|球徑|da|dp",
        "珠卷數": r"卷數|卷数|圈數|turns|count",
        "動負荷 C (kfg)": r"動|动|ca(?:\s|_|$)|C\(|C\s|dynamic",
        "靜負荷 Co (kfg)": r"靜|静|co(?:\s|_|$)|Co\(|Co\s|static",
        "剛性 kfg/umk": r"剛性|刚性|rigidity|k(?:\s|_|$)",
    }
    
    # 對每一列進行模糊比對
    for col in final_pmi.columns:
        col_lower = col.lower().strip()
        for standard_name, pattern in mapping_rules.items():
            if re.search(pattern, col_lower, re.IGNORECASE):
                rename_dict[col] = standard_name
                break
    
    # 重新命名
    final_pmi = final_pmi.rename(columns=rename_dict)
    
    # 移除完全重複的欄位名稱
    final_pmi = final_pmi.loc[:, ~final_pmi.columns.duplicated()]
    
    # --- 過濾重複欄位（保留第一個） ---
    # 方法：對每個重複欄位只保留第一列
    cols_seen = {}
    cols_to_keep = []
    for col in final_pmi.columns:
        if col not in cols_seen:
            cols_seen[col] = True
            cols_to_keep.append(col)
        else:
            # 重複欄位，跳過
            pass
    final_pmi = final_pmi[cols_to_keep]
    
    print(f"[Debug] 重新命名後欄位數：{len(final_pmi.columns)}")
    print(f"[Debug] 最終欄位：{final_pmi.columns.tolist()}")
    print(f"[Debug] 重組前行數：{len(final_pmi)}")
    
    # --- 補上缺失的標準欄位 ---
    expected_cols = [
        "Series_Name", "Source_Page", "型號", "公稱 外徑", "導程", 
        "珠徑", "珠卷數", "動負荷 C (kfg)", "靜負荷 Co (kfg)", "剛性 kfg/umk"
    ]
    
    for col in expected_cols:
        if col not in final_pmi.columns:
            final_pmi[col] = pd.NA
    
    # 重新排列欄位順序
    final_pmi = final_pmi[expected_cols]
    
    # --- 移除表頭殘影 ---
    # 過濾掉「公稱 外徑」欄位中包含英文字母的列
    before_filter = len(final_pmi)
    if "公稱 外徑" in final_pmi.columns:
        final_pmi = final_pmi[
            ~final_pmi["公稱 外徑"].astype(str).str.contains(r'[A-Za-z]', na=False)
        ].reset_index(drop=True)
    print(f"[Debug] 過濾英文字母後：{before_filter} → {len(final_pmi)} 行")
    
    # 確保型號不為空
    before_filter = len(final_pmi)
    final_pmi = final_pmi[final_pmi["型號"].notna() & (final_pmi["型號"] != "")].reset_index(drop=True)
    print(f"[Debug] 過濾空型號後：{before_filter} → {len(final_pmi)} 行")
    
    # --- 轉換資料型態 ---
    numeric_cols = [
        "公稱 外徑", "導程", "珠徑", "珠卷數", 
        "動負荷 C (kfg)", "靜負荷 Co (kfg)", "剛性 kfg/umk"
    ]
    available_numeric_cols = [col for col in numeric_cols if col in final_pmi.columns]
    final_pmi = change_astype_robust(final_pmi, available_numeric_cols)
    
    # --- 向下填充 ---
    final_pmi = final_pmi.ffill()
    
    # --- 注入品牌標籤 ---
    final_pmi['brand'] = "PMI"
    final_pmi['category'] = "Screw"
    final_pmi['data_type'] = "Specification"
    
    # --- 創建別名以兼容應用 ---
    final_pmi['Ca'] = final_pmi.get('動負荷 C (kfg)', pd.NA)
    final_pmi['Co'] = final_pmi.get('靜負荷 Co (kfg)', pd.NA)
    final_pmi['Model'] = final_pmi.get('型號', pd.NA)
    final_pmi['Diameter'] = final_pmi.get('公稱 外徑', pd.NA)
    final_pmi['Lead'] = final_pmi.get('導程', pd.NA)
    
    # --- 產生語意欄位 ---
    def generate_pmi_semantic(row):
        return (
            f"這是銀泰 (PMI) 的滾珠螺桿規格。系列名稱為 {row.get('Series_Name', 'Unknown')}，"
            f"完整型號為 {row.get('型號', 'N/A')}。其主要參數如下：公稱外徑為 {row.get('公稱 外徑', 'N/A')} mm，"
            f"導程為 {row.get('導程', 'N/A')} mm，珠徑為 {row.get('珠徑', 'N/A')} mm，珠卷數為 {row.get('珠卷數', 'N/A')}。"
            f"在性能指標方面，其動負荷 (Ca) 為 {row.get('動負荷 C (kfg)', 'N/A')} kgf，"
            f"靜負荷 (Co) 為 {row.get('靜負荷 Co (kfg)', 'N/A')} kgf，剛性為 {row.get('剛性 kfg/umk', 'N/A')} kgf/umk。"
        )
    
    final_pmi['semantic_text'] = final_pmi.apply(generate_pmi_semantic, axis=1)
    
    # --- 輸出驗證 ---
    if final_pmi is not None and not final_pmi.empty:
        # Validate critical columns
        critical_cols = ["型號", "公稱 外徑", "導程"]
        missing_cols = [col for col in critical_cols if col not in final_pmi.columns]
        
        if missing_cols:
            print(f"⚠️ 警告: 缺失關鍵欄位 {missing_cols}")
            return None
        
        # Check for all-NaN columns
        all_nan_cols = final_pmi.columns[final_pmi.isna().all()].tolist()
        if all_nan_cols:
            print(f"⚠️ 警告: 以下欄位全為空值 {all_nan_cols}")
        
        # Validate numeric conversion
        numeric_issues = []
        for col in ["公稱 外徑", "導程", "動負荷 C (kfg)", "靜負荷 Co (kfg)"]:
            if col in final_pmi.columns:
                nan_count = final_pmi[col].isna().sum()
                if nan_count > 0:
                    numeric_issues.append(f"{col} ({nan_count} NaN)")
        
        if numeric_issues:
            print(f"⚠️ 數值轉換問題: {numeric_issues}")
    else:
        print("🔴 致命錯誤: 最終 DataFrame 為空!")
        return None
    
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

    # 確保輸出目錄存在
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    # 判斷品牌
    if "PMI" in pdf_path.upper() or "銀泰" in pdf_path:
        brand = "PMI"
        print("開始處理銀泰 (PMI) 表格...\n")
        all_processed_tables = process_pmi_tables(pdf_path)
        if all_processed_tables:
            final_df = build_final_pmi_df(all_processed_tables)
            output_file = output_dir / "PMI_Final_Data_V3.xlsx"
        else:
            final_df = None
    else:
        brand = "HIWIN"
        print("開始處理上銀 (HIWIN) 表格...\n")
        final_hiwin_df = process_and_view(pdf_path)
        if final_hiwin_df:
            final_df = build_final_hiwin_df(final_hiwin_df)
            output_file = output_dir / "HIWIN_Final_Data_V1.xlsx"
        else:
            final_df = None

    if final_df is not None:
        try:
            final_df.to_excel(output_file, index=False)
            print("資料清洗完成！")
            print(f"已輸出：{output_file}")
        except PermissionError as e:
            print(f"錯誤：無法寫入 Excel 檔案 (檔案可能被打開)：{e}")
            print(f"建議：請關閉 Excel 中的 {output_file}，然後重新執行")
        except Exception as e:
            print(f"錯誤：無法輸出檔案：{e}")
        print(final_df.head(30))
    else:
        print("沒有可處理的表格。")