# 03_embeddings - ChromaDB 與 RAG 資料庫

此資料夾負責檢查、實驗與重建 ChromaDB 向量資料庫。目前正式使用的資料庫位於根目錄 `databases/hiwin_vector_db/`，主要 collection 名稱為 `screw_specs`。

## 目前內容

```text
03_embeddings/
├── notebooks/
│   ├── chromadb資料庫處理與整合.ipynb
│   └── embeding 工程.ipynb
├── scripts/
│   └── update_rag_specs.py
└── README.md
```

## Notebook 說明

| 檔案 | 實際內容 |
| --- | --- |
| `chromadb資料庫處理與整合.ipynb` | 連接 `hiwin_vector_db`，列出 collections，檢查 `screw_specs` 內容並 peek 部分資料。 |
| `embeding 工程.ipynb` | 較早期的 embedding 實驗。包含 BGE-M3 / SentenceTransformer embedding、建立 `hiwin_manual`、`hiwin_specs` 等 collection，以及 Excel `semantic_text` 寫回實驗。 |

## Script 說明

### `update_rag_specs.py`

目前建議使用的正式資料庫重建腳本。它會讀取 Excel 規格資料與型錄 chunk，重建 ChromaDB collection：

```text
databases/hiwin_vector_db
└── collection: screw_specs
```

資料來源：

- `data/HIWIN_Final_Data_V1.xlsx`
- `data/PMI_Optimized_Core.xlsx`
- `data/FANUC_Specs.xlsx`
- `code/outputs/HIWIN_final_chunks.json`
- `code/outputs/PMI_final_chunks.json`
- `code/outputs/FANUC_final_chunks.json`

寫入的資料類型包含：

- HIWIN/PMI 螺桿規格：`data_type = Specification`
- FANUC 馬達型號與詳細資料：`category = Motor`
- HIWIN/PMI/FANUC 手冊 chunk：`data_type = Manual`

## 建議執行方式

從專案根目錄執行：

```powershell
python code/03_embeddings/scripts/update_rag_specs.py --dry-run
```

確認資料都能讀取後，再正式重建：

```powershell
python code/03_embeddings/scripts/update_rag_specs.py
```

正式執行會刪除並重建 `screw_specs` collection。

## 資料庫檢查

可以使用 notebook：

```text
code/03_embeddings/notebooks/chromadb資料庫處理與整合.ipynb
```

或在應用端透過 `04_applications/scripts/LLM connection test.py` 檢查資料類型統計與互動問答。

## 與應用端的關係

`04_applications/scripts/app_simple_v3.py` 會讀取：

```text
databases/hiwin_vector_db
collection: screw_specs
```

如果 Streamlit RAG 查不到資料，請先確認：

1. `update_rag_specs.py --dry-run` 能正常列出資料筆數。
2. 正式重建後 `screw_specs` collection count 大於 0。
3. 執行 Streamlit 時目前工作目錄在專案根目錄。

## 維護注意事項

- 更新 `data/*.xlsx` 或 `code/outputs/*_final_chunks.json` 後，要重新執行 `update_rag_specs.py`。
- `embeding 工程.ipynb` 內部分 collection 名稱與路徑屬於早期實驗，不代表目前應用端實際讀取的 collection。
- 目前 `update_rag_specs.py` 使用 ChromaDB 內建文件寫入與查詢流程，沒有在 script 中指定 OpenAI embedding。
