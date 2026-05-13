# 04_applications - Streamlit 選型系統與 LLM/RAG 應用

此資料夾負責把前面整理好的 Excel 規格資料與 ChromaDB RAG 資料庫串成可互動的應用。目前主要應用是 Streamlit 智慧選型介面，並透過 Ollama 進行本地 LLM 技術諮詢。

## 目前內容

```text
04_applications/
├── notebooks/
│   └── LLM串接工程.ipynb
├── scripts/
│   ├── app_simple.py
│   ├── app_simple_v3.py
│   └── LLM connection test.py
└── README.md
```

## Notebook 說明

| 檔案 | 實際內容 |
| --- | --- |
| `LLM串接工程.ipynb` | ChromaDB 連線、`screw_specs` collection 檢索、Ollama Qwen/Gemma prompt 測試、RAG 與非 RAG 回答比較、檢索能力檢查。 |

## Script 說明

| 檔案 | 用途 | 狀態 |
| --- | --- | --- |
| `app_simple_v3.py` | 目前主要 Streamlit 應用。讀取 HIWIN/PMI/FANUC Excel，計算螺桿與馬達選型參數，推薦型號，並提供 RAG 技術諮詢。 | 建議使用 |
| `app_simple.py` | 早期 Streamlit UI 原型。多數計算結果是固定示範值，RAG 尚未完成。 | 保留參考 |
| `LLM connection test.py` | 命令列測試工具。連接 `screw_specs`，統計資料類型，並以 Ollama `gemma3n:e4b` 做互動問答測試。 | 測試/除錯用 |

## 主要輸入

`app_simple_v3.py` 會從專案根目錄讀取：

- `data/HIWIN_Final_Data_V1.xlsx`
- `data/PMI_Optimized_Core.xlsx`
- `data/FANUC_Specs.xlsx`
- `databases/hiwin_vector_db`

RAG collection：

```text
collection: screw_specs
```

如果資料庫尚未建立或需要更新，請先回到專案根目錄執行：

```powershell
python code/03_embeddings/scripts/update_rag_specs.py
```

## 啟動 Streamlit 應用

從專案根目錄執行：

```powershell
streamlit run code/04_applications/scripts/app_simple_v3.py
```

介面包含：

- 使用者設計條件輸入
- 導程、螺桿最高轉速、直徑範圍、動負荷等計算
- HIWIN/PMI 螺桿推薦
- FANUC 馬達匹配
- 自定義規格探索
- RAG 技術諮詢聊天視窗

## Ollama 需求

`app_simple_v3.py` 與 `LLM connection test.py` 都使用 Ollama。請先確認：

```powershell
ollama list
```

目前程式中的模型名稱：

- `app_simple_v3.py`：`gemma2:9b`
- `LLM connection test.py`：`gemma3n:e4b`
- `LLM串接工程.ipynb`：包含 `qwen2.5:7b` 與 `gemma3n:e4b` 測試片段

如果本機模型名稱不同，需要同步修改程式中的 `ollama.chat()` 或 `ollama.generate()` model 參數。

## RAG 流程

```text
使用者問題
  ↓
ChromaDB screw_specs 檢索
  ↓
取得規格資料與手冊 chunk
  ↓
組合目前選型計算結果與檢索內容
  ↓
送入 Ollama 模型
  ↓
回傳技術建議
```

## 除錯方式

### 檢查資料庫是否可讀

```powershell
python code/03_embeddings/scripts/update_rag_specs.py --dry-run
```

### 重新建立資料庫

```powershell
python code/03_embeddings/scripts/update_rag_specs.py
```

### 測試 Ollama 與 RAG 連線

```powershell
python "code/04_applications/scripts/LLM connection test.py"
```

## 維護注意事項

- 執行 Streamlit 時請在專案根目錄，否則 `data/*.xlsx` 可能讀不到。
- 如果 RAG 回答顯示功能不可用，請確認 `chromadb`、`ollama` 套件已安裝，且 Ollama 服務正在執行。
- 更新 Excel 或 `code/outputs/*_final_chunks.json` 後，要先重建 `screw_specs`。
- `app_simple.py` 不是目前主線版本，文件與測試請以 `app_simple_v3.py` 為準。
