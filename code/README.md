# code 資料夾說明

此資料夾收納 Feed System GAI 的主要開發流程：型錄擷取、規格資料處理、向量資料庫建置，以及 Streamlit/LLM 應用。專案目前的核心資料來源放在根目錄 `data/`，RAG 資料庫放在根目錄 `databases/hiwin_vector_db/`。

## 目錄結構

```text
code/
├── 01_extraction/        # PDF 文字、公式與初步 chunk 擷取
├── 02_processing/        # 規格表處理、參數轉換、semantic_text 建立
├── 03_embeddings/        # ChromaDB 檢查與 screw_specs collection 重建
├── 04_applications/      # Streamlit 選型系統與 Ollama RAG 應用
├── outputs/              # 已產生的擷取結果與檢查報告
├── HIWIN_Extracted_Data.xlsx
├── 銀泰螺桿型錄 切割 共67頁.pdf
└── README.md
```

## 流程總覽

```text
data/*.pdf
  ↓
01_extraction
PDF 文字、公式、手冊段落擷取，產生 JSON/Markdown chunk
  ↓
02_processing
HIWIN/PMI/FANUC 規格表清理與計算欄位整理
  ↓
03_embeddings
讀取 data/*.xlsx 與 code/outputs/*_final_chunks.json，重建 ChromaDB
  ↓
04_applications
Streamlit 介面進行選型、推薦與 RAG 技術諮詢
```

## 各子資料夾重點

| 資料夾 | 目前內容 | 重點檔案 |
| --- | --- | --- |
| `01_extraction` | PDF 擷取 notebook、PyMuPDF 擷取 script、OpenDataLoader 測試 script | `文字說明內容擷取(上銀 銀泰 FUNAC) V2.py` |
| `02_processing` | HIWIN 表格整理 notebook、參數計算 notebook、PMI 表格擷取 script | `PMI型錄表格擷取優化.py` |
| `03_embeddings` | ChromaDB 檢查 notebook、embedding 實驗 notebook、資料庫重建 script | `update_rag_specs.py` |
| `04_applications` | Streamlit app、Ollama RAG 測試 script、LLM notebook | `app_simple_v3.py` |
| `outputs` | 既有擷取結果、chunk 視覺化、extraction check 報告 | `*_final_chunks.json` |

## 建議從專案根目錄執行

多數應用程式會用相對路徑讀取 `data/` 與 `databases/`，建議命令都從專案根目錄執行：

```powershell
cd "C:\Users\e11338\Desktop\Feed System GAI"
.\venv\Scripts\Activate.ps1
```

## 常用命令

### 檢查或重建 RAG 資料庫

```powershell
python code/03_embeddings/scripts/update_rag_specs.py --dry-run
python code/03_embeddings/scripts/update_rag_specs.py
```

`update_rag_specs.py` 會重建 `databases/hiwin_vector_db` 內的 `screw_specs` collection，資料來源包含：

- `data/HIWIN_Final_Data_V1.xlsx`
- `data/PMI_Optimized_Core.xlsx`
- `data/FANUC_Specs.xlsx`
- `code/outputs/HIWIN_final_chunks.json`
- `code/outputs/PMI_final_chunks.json`
- `code/outputs/FANUC_final_chunks.json`

### 啟動主要 Streamlit 應用

```powershell
streamlit run code/04_applications/scripts/app_simple_v3.py
```

`app_simple_v3.py` 會讀取根目錄的 `data/*.xlsx` 與 `databases/hiwin_vector_db`。RAG 回答使用 Ollama，程式中目前預設模型為 `gemma2:9b`。

### 重新擷取型錄文字與公式

此 script 的輸出位置取決於執行時的目前目錄。若希望輸出集中到 `code/outputs/`，建議這樣執行：

```powershell
Push-Location code/outputs
python ../01_extraction/scripts/"文字說明內容擷取(上銀 銀泰 FUNAC) V2.py"
Pop-Location
```

## 注意事項

- `code/outputs` 內已有一批現成的 `HIWIN/PMI/FANUC_final_chunks.json`，目前 RAG 重建會使用這些檔案。
- `02_processing/scripts/PMI型錄表格擷取優化.py` 的內建預設 PDF 路徑不是目前 Windows 專案路徑，請執行時明確傳入 `--pdf` 與 `--output`。
- `04_applications/scripts/app_simple.py` 是較早期的靜態 UI 原型；目前較完整的版本是 `app_simple_v3.py`。
- `03_embeddings/notebooks/embeding 工程.ipynb` 保留了較早期的 embedding 實驗，正式更新資料庫建議使用 `scripts/update_rag_specs.py`。
