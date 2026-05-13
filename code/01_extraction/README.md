# 01_extraction - PDF 文字、公式與手冊段落擷取

此資料夾負責從 HIWIN、PMI、FANUC 型錄 PDF 擷取可供後續 RAG 使用的文字說明、公式與手冊段落。表格規格的正式整理主要放在 `02_processing`。

## 目前內容

```text
01_extraction/
├── notebooks/
│   ├── 上銀型錄文字擷取.ipynb
│   ├── 銀泰型錄文字擷取.ipynb
│   └── 馬達資料處裡.ipynb
├── scripts/
│   ├── PDF-Txtration-Tool-Test.py
│   ├── 文字說明內容擷取(上銀 銀泰 FUNAC).py
│   └── 文字說明內容擷取(上銀 銀泰 FUNAC) V2.py
└── README.md
```

## Notebook 說明

| 檔案 | 實際內容 |
| --- | --- |
| `上銀型錄文字擷取.ipynb` | 使用 PyMuPDF 讀取上銀 PDF，進行頁面文字擷取、表格/雜訊過濾、語意 chunk 切分與 Markdown/JSON 檢查輸出。 |
| `銀泰型錄文字擷取.ipynb` | 與上銀流程類似，用於銀泰 PDF 的文字擷取、清理與 chunk 化。 |
| `馬達資料處裡.ipynb` | 針對 FANUC 伺服馬達型錄資料進行擷取與整理實驗，重點是馬達規格資料。 |

## Script 說明

| 檔案 | 用途 | 備註 |
| --- | --- | --- |
| `文字說明內容擷取(上銀 銀泰 FUNAC) V2.py` | 目前建議使用的批次擷取腳本。讀取 HIWIN、PMI、FANUC 三份 PDF，過濾表格頁與數字噪音，輸出文字/公式 JSON 與 Markdown。 | PDF 路徑目前寫死為專案根目錄 `data/` 下的三份 PDF。 |
| `文字說明內容擷取(上銀 銀泰 FUNAC).py` | 舊版批次擷取腳本。邏輯與 V2 類似，但頁面/段落過濾條件較早期。 | 保留作為比較或回溯。 |
| `PDF-Txtration-Tool-Test.py` | 使用 `opendataloader_pdf.convert()` 測試 PDF 轉 json/html/pdf/markdown。 | 目前是工具測試腳本，並非主流程。 |

## 主要輸入

腳本目前對應的 PDF：

- `data/B65542EN_01_ai-D伺服馬達仕樣.pdf`
- `data/上銀滾珠螺桿.pdf`
- `data/銀泰螺桿型錄.pdf`

## 建議執行方式

`V2.py` 的輸出檔會寫到「執行命令當下所在的資料夾」。若要讓輸出集中在 `code/outputs/`，建議從專案根目錄執行：

```powershell
Push-Location code/outputs
python ../01_extraction/scripts/"文字說明內容擷取(上銀 銀泰 FUNAC) V2.py"
Pop-Location
```

輸出檔格式：

```text
catalog_text_formula_extraction_YYYYMMDD_HHMMSS.json
catalog_text_formula_extraction_YYYYMMDD_HHMMSS.md
```

## 目前已存在的相關輸出

既有成果目前集中在 `code/outputs/`：

- `catalog_text_formula_extraction_20260420_160730.json`
- `catalog_text_formula_extraction_20260420_160730.md`
- `HIWIN_final_chunks.json`
- `PMI_final_chunks.json`
- `FANUC_final_chunks.json`
- `*_extraction_check.md`
- `*_chunking_visualization.md`

其中 `*_final_chunks.json` 會被 `03_embeddings/scripts/update_rag_specs.py` 讀取，用來建立 `Manual` 類型的 RAG 資料。

## 維護注意事項

- 新增 PDF 時，請先更新 `CATALOGS` 內的路徑與品牌名稱。
- 如果擷取內容太少，優先檢查 `is_table_heavy_page()`、`is_page_useful()` 與段落過濾條件。
- 如果輸出沒有出現在 `code/outputs/`，通常是因為執行命令時所在目錄不同。
- Notebook 適合探索與調整規則；批次產出建議使用 `V2.py`。
