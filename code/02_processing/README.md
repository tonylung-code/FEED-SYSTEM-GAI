# 02_processing - 規格資料處理與參數計算

此資料夾負責把擷取到的表格與規格資料整理成可供選型、推薦與 RAG 使用的結構化資料。主要處理內容包含 HIWIN 表格清理、PMI 表格擷取、參數公式試算，以及建立 `semantic_text` 欄位。

## 目前內容

```text
02_processing/
├── notebooks/
│   ├── 上銀表格處裡.ipynb
│   ├── 參數比對.ipynb
│   └── 參數轉換公式.ipynb
├── scripts/
│   └── PMI型錄表格擷取優化.py
└── README.md
```

## Notebook 說明

| 檔案 | 實際內容 |
| --- | --- |
| `上銀表格處裡.ipynb` | HIWIN 表格擷取與清理實驗。包含 PDF 文字座標排序、系列名稱擷取、表格欄位整理、數值轉換、`semantic_text` 生成與 Excel 輸出。 |
| `參數比對.ipynb` | 將不同系列 sheet 合併或比對，並根據使用者輸入條件試算導程、螺桿最高轉速、直徑範圍、動負荷等選型參數。 |
| `參數轉換公式.ipynb` | 保存與驗證選型計算公式，例如導程、臨界轉速、挫曲負荷、動負荷、馬達扭矩與慣量等計算邏輯。 |

## Script 說明

### `PMI型錄表格擷取優化.py`

PMI 銀泰型錄表格擷取與清理腳本。它會從 PDF 表格中整理出下列欄位：

- `Series_Name`
- `Source_Page`
- `型號`
- `外徑`
- `導程`
- `鋼珠直徑`
- `循環圈數`
- `動負荷`
- `靜負荷`
- `剛性`
- `semantic_text`

建議從專案根目錄明確指定輸入與輸出：

```powershell
python code/02_processing/scripts/PMI型錄表格擷取優化.py --pdf data/銀泰螺桿型錄.pdf --output data/PMI_Optimized_Core.xlsx
```

注意：此 script 內建的 `--pdf` 預設值是舊的 Mac 路徑，不符合目前 Windows 專案位置；請務必傳入 `--pdf`。

## 主要輸入與輸出

| 類型 | 檔案 |
| --- | --- |
| PMI 原始 PDF | `data/銀泰螺桿型錄.pdf` |
| PMI 正式輸出 | `data/PMI_Optimized_Core.xlsx` |
| HIWIN 整理後資料 | `data/HIWIN_Final_Data_V1.xlsx` |
| FANUC 整理後資料 | `data/FANUC_Specs.xlsx` |
| 其他既有輸出 | `outputs/PMI_Optimized_Core.xlsx`、`code/HIWIN_Extracted_Data.xlsx` |

## 與後續流程的關係

`03_embeddings/scripts/update_rag_specs.py` 會讀取下列正式資料：

- `data/HIWIN_Final_Data_V1.xlsx`
- `data/PMI_Optimized_Core.xlsx`
- `data/FANUC_Specs.xlsx`

因此只要更新了這些 Excel，請重新執行：

```powershell
python code/03_embeddings/scripts/update_rag_specs.py
```

## 維護注意事項

- `semantic_text` 是 RAG 與推薦說明的重要欄位，更新規格表時要確認仍有產生。
- Notebook 中部分路徑是早期本機測試路徑，正式執行建議改成專案根目錄下的 `data/`。
- 若 PMI 擷取列數異常，優先檢查 PDF 是否為同版型，以及 `looks_like_main_table()`、欄位位置與頁面表格線設定。
