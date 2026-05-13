# Feed System GAI

工業型錄資料擷取、規格整理、向量資料庫與 RAG 查詢應用專案。此專案目前聚焦在 HIWIN 上銀滾珠螺桿、PMI 銀泰螺桿，以及 FANUC 伺服馬達規格資料，目標是把 PDF/Excel 型錄資料整理成可查詢、可推薦、可串接 LLM 的工程選型輔助系統。

## 專案目標

- 從工業 PDF 型錄擷取文字說明、公式、規格表與產品資料。
- 將 HIWIN、PMI、FANUC 的規格資料整理成 Excel 與 JSON 中間資料。
- 建立 ChromaDB 向量資料庫，支援型錄內容與規格資料檢索。
- 提供 Streamlit 介面，進行螺桿/馬達選型、參數計算與 RAG 問答。

## 目前資料夾結構

```text
Feed System GAI/
├── code/                         # 程式碼、notebook、流程文件與中間輸出
│   ├── 01_extraction/             # PDF 文字、公式與表格擷取
│   ├── 02_processing/             # 規格表清理、參數轉換與資料加工
│   ├── 03_embeddings/             # ChromaDB 建置與 RAG 資料更新
│   ├── 04_applications/           # Streamlit/LLM 應用
│   ├── outputs/                   # 擷取後的 JSON/Markdown 檢查檔
│   ├── README.md                  # code 資料夾原有流程說明
│   └── HIWIN_Extracted_Data.xlsx  # 擷取或處理過的上銀資料
├── data/                          # 原始 PDF 與整理後的核心 Excel 資料
│   ├── 上銀滾珠螺桿.pdf
│   ├── 銀泰螺桿型錄.pdf
│   ├── B65542EN_01_ai-D伺服馬達仕樣.pdf
│   ├── HIWIN_Final_Data_V1.xlsx
│   ├── PMI_Optimized_Core.xlsx
│   └── FANUC_Specs.xlsx
├── databases/                     # ChromaDB 持久化資料
│   └── hiwin_vector_db/
├── outputs/                       # 根目錄層級的輸出檔，目前含 PMI Excel 結果
├── requirements.txt               # Python 套件清單
├── Dockerfile                     # 容器化環境設定
├── Modelfile                      # Ollama/本地模型設定
├── 建立python虛擬環境步驟.txt
├── 寫入GitHub步驟.txt
└── 上銀螺桿型錄分類.txt
```

## 子資料夾說明

| 位置 | 內容 | 主要用途 |
| --- | --- | --- |
| `code/01_extraction` | 擷取 notebooks 與 scripts | 從 HIWIN、PMI、FANUC PDF 擷取文字、公式、表格與檢查檔 |
| `code/02_processing` | 參數轉換 notebooks、PMI 表格擷取 script | 清理規格表、建立 `semantic_text`、整理可供推薦與 RAG 使用的欄位 |
| `code/03_embeddings` | ChromaDB notebooks、`update_rag_specs.py` | 將 Excel 規格與型錄 chunk 寫入 `databases/hiwin_vector_db` |
| `code/04_applications` | LLM notebook、Streamlit apps | 提供智慧選型、規格推薦、Ollama RAG 問答介面 |
| `data` | PDF 與正式 Excel 資料 | 建議作為主要資料來源入口 |
| `code/outputs` | JSON/Markdown 中間結果 | 用於檢查擷取品質與建立型錄文字 chunk |
| `databases` | ChromaDB 檔案 | RAG 檢索資料庫，不建議手動修改 |

## 快速開始

### 1. 建立與啟用環境

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

如果已經有 `venv/`，可直接啟用：

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. 更新 RAG 向量資料庫

此步驟會讀取：

- `data/HIWIN_Final_Data_V1.xlsx`
- `data/PMI_Optimized_Core.xlsx`
- `data/FANUC_Specs.xlsx`
- `code/outputs/*_final_chunks.json`

並重建 ChromaDB collection：`screw_specs`。

```powershell
python code/03_embeddings/scripts/update_rag_specs.py
```

只檢查資料筆數、不寫入資料庫：

```powershell
python code/03_embeddings/scripts/update_rag_specs.py --dry-run
```

### 3. 啟動 Streamlit 應用

主要應用建議使用 `app_simple_v3.py`：

```powershell
streamlit run code/04_applications/scripts/app_simple_v3.py
```

此應用會讀取：

- `data/HIWIN_Final_Data_V1.xlsx`
- `data/PMI_Optimized_Core.xlsx`
- `data/FANUC_Specs.xlsx`
- `databases/hiwin_vector_db`

RAG 問答目前使用 `ollama`，程式中預設模型為 `gemma2:9b`。如果要啟用本地問答，請確認 Ollama 已啟動且模型已存在。

## 主要工作流程

```text
原始型錄 PDF / Excel
        ↓
01_extraction
擷取文字、公式、表格
        ↓
02_processing
清理欄位、整理規格、產生語意描述
        ↓
03_embeddings
建立或更新 ChromaDB 向量資料庫
        ↓
04_applications
Streamlit 選型系統與 RAG 問答
```

## 常用腳本

| 指令 | 用途 |
| --- | --- |
| `python "code/01_extraction/scripts/文字說明內容擷取(上銀 銀泰 FUNAC) V2.py"` | 擷取 HIWIN、PMI、FANUC 型錄文字與公式 |
| `python code/02_processing/scripts/PMI型錄表格擷取優化.py --pdf data/銀泰螺桿型錄.pdf --output data/PMI_Optimized_Core.xlsx` | 從 PMI PDF 擷取並整理規格表 |
| `python code/03_embeddings/scripts/update_rag_specs.py --dry-run` | 檢查 RAG 資料來源是否可讀 |
| `python code/03_embeddings/scripts/update_rag_specs.py` | 重建 ChromaDB `screw_specs` collection |
| `streamlit run code/04_applications/scripts/app_simple_v3.py` | 啟動智慧選型與 RAG 問答介面 |

## 重要資料檔

| 檔案 | 角色 |
| --- | --- |
| `data/HIWIN_Final_Data_V1.xlsx` | 上銀螺桿正式規格資料 |
| `data/PMI_Optimized_Core.xlsx` | 銀泰螺桿正式規格資料 |
| `data/FANUC_Specs.xlsx` | FANUC 馬達規格資料 |
| `code/outputs/HIWIN_final_chunks.json` | 上銀型錄文字 chunk |
| `code/outputs/PMI_final_chunks.json` | 銀泰型錄文字 chunk |
| `code/outputs/FANUC_final_chunks.json` | FANUC 型錄文字 chunk |
| `databases/hiwin_vector_db` | ChromaDB 持久化資料庫 |

## 建議的資料夾整理方向

目前的流程已經大致清楚，但有幾個地方可以再整理，讓後續維護更穩：

### 建議 1：把所有輸出集中到根目錄 `outputs/`

目前同時存在 `outputs/` 與 `code/outputs/`，容易混淆。建議改成：

```text
outputs/
├── extraction/       # PDF 擷取後的 JSON/Markdown
├── processed/        # 清理後 Excel/CSV
└── reports/          # 檢查報告、視覺化 markdown
```

優點：輸出集中、備份與清理容易。  
注意：需要同步修改 scripts 中的輸出路徑。

### 建議 2：把原始資料與正式整理資料分開

目前 `data/` 同時放原始 PDF 與整理後 Excel。建議改成：

```text
data/
├── raw/              # 原始 PDF
├── processed/        # 正式 Excel 規格資料
└── reference/        # 分類、對照、人工整理文件
```

優點：可以清楚分辨哪些是原始資料、哪些是可被應用程式讀取的正式資料。  
注意：`app_simple_v3.py` 與 `update_rag_specs.py` 目前直接讀 `data/*.xlsx`，搬移前要先改路徑。

### 建議 3：把開發紀錄文件移到 `docs/`

根目錄目前有：

- `建立python虛擬環境步驟.txt`
- `寫入GitHub步驟.txt`
- `上銀螺桿型錄分類.txt`

建議整理為：

```text
docs/
├── setup.md
├── github-workflow.md
└── hiwin-catalog-classification.md
```

優點：根目錄更乾淨，也比較符合一般專案閱讀習慣。

### 建議 4：避免把 `venv/` 放進專案同步範圍

目前專案中有 `venv/`。如果這個資料夾只是本機環境，建議保留在本機但不要納入 Git。`.gitignore` 應包含：

```gitignore
venv/
__pycache__/
.env
```

## 建議的新結構草案

如果要整理，我建議往這個方向走：

```text
Feed System GAI/
├── README.md
├── requirements.txt
├── Dockerfile
├── Modelfile
├── code/
│   ├── 01_extraction/
│   ├── 02_processing/
│   ├── 03_embeddings/
│   └── 04_applications/
├── data/
│   ├── raw/
│   ├── processed/
│   └── reference/
├── outputs/
│   ├── extraction/
│   ├── processed/
│   └── reports/
├── databases/
│   └── hiwin_vector_db/
└── docs/
    ├── setup.md
    ├── github-workflow.md
    └── hiwin-catalog-classification.md
```

目前我建議先不要直接搬檔，因為多個 scripts 仍使用固定路徑。可以先確認你想採用哪個整理方案，再逐步修改路徑與測試流程。

## 維護注意事項

- 更新 Excel 規格後，請重新執行 `update_rag_specs.py`。
- 更新 PDF 型錄後，請先重新跑 `01_extraction`，確認 `code/outputs/*_final_chunks.json` 正常，再更新 ChromaDB。
- 如果 Streamlit 啟動後找不到資料，優先檢查目前執行位置是否在專案根目錄。
- 如果 RAG 問答不可用，確認 `chromadb`、`ollama` 已安裝，且 Ollama 模型 `gemma2:9b` 可使用。

