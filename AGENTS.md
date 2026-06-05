# Feed System GAI Agent 工作指南

本文件是給 Codex / AI Agent 使用的專案工作指南。開始任何修改前，請先閱讀本文件，並以此作為專案範圍、測試方式與安全規範的依據。

## 專案背景

Feed System GAI 是進給系統智慧選型專案，主要功能包含：

- 滾珠螺桿與馬達規格推薦
- 使用者設計條件計算
- 馬達規格圖與尺寸圖查詢
- PDF 規格資料查詢
- LLM / RAG 技術助理

目前專案同時包含正式測試中的 Streamlit UI、計算模組、RAG 實驗腳本、型錄資料、向量資料庫與歷史處理流程。後續 Agent 應優先保護資料檔、歷史腳本、向量資料與使用者尚未提交的工作內容。

## 專案目錄說明

### 主要開發區

`code/UI_test`

這是目前唯一主要開發與測試區域。除非使用者另有要求，Agent 應優先在此區域進行修改。

### 參考資料區

以下目錄預設視為資料來源、歷史流程或處理產物，非必要請勿修改：

- `data`
- `databases`
- `code/01_extraction`
- `code/02_processing`
- `code/03_embeddings`
- `code/04_applications`
- `code/outputs`
- `outputs`

若任務必須修改上述區域，請先說明原因、影響範圍與測試方式。

## Streamlit 啟動規範

主要啟動指令：

```bash
streamlit run code/UI_test/UI_segmentation.py
```

專案固定使用：

```text
http://localhost:8888
```

Streamlit 設定檔位於 `.streamlit/config.toml`：

```toml
[server]
port = 8888
headless = true

[browser]
gatherUsageStats = false
```

除非使用者明確要求，不得修改 Streamlit Port。若 Port `8888` 被占用，應提示使用者，不得自動改成 `8501`、`8502`、`8503` 或其他 Port。

## 主要模組說明

### `code/UI_test/UI_segmentation.py`

Streamlit UI 入口，包含：

- 智慧選型與推薦系統
- 使用者設計條件輸入
- 螺桿與馬達推薦結果顯示
- 馬達規格圖片顯示
- AI 技術助理頁籤

### `code/UI_test/Formula_set_lookup.py`

核心計算模組，包含：

- 滾珠螺桿導程、外徑與動負荷計算
- 安全驗證
- 剛性計算
- 慣量計算
- 馬達匹配

此檔目前存在部分絕對路徑。搬移專案或整理路徑前，應逐步改為相對路徑，並優先透過 `ui_paths.py` 集中管理。

### `code/UI_test/llm_rag_service.py`

LLM / RAG 服務模組，包含：

- 本機 `.npz` 向量資料檢索
- 關鍵字搜尋與可選語意搜尋
- RAG Context 組裝
- Ollama 查詢
- 本機 Ollama 模型列表

### `code/UI_test/ui_paths.py`

UI 測試區路徑管理模組，包含：

- 專案根目錄定位
- `data` 資料路徑
- `LLM code/vector_data` 路徑
- 馬達規格圖片路徑
- PDF 頁面與圖片對應邏輯

若需要新增或修改資料路徑，優先修改此檔，避免在多個檔案中硬編碼路徑。

### `code/UI_test/LLM code/test_001.py`

向量資料產生與 PDF 圖片擷取實驗腳本，包含：

- PDF 頁面轉圖片
- JSON 轉單元資料
- 使用 `BAAI/bge-m3` 建立 embedding
- 輸出 `.npz` 向量資料

### `code/UI_test/LLM code/test_002.py`

RAG 驗證與 Ollama 查詢實驗腳本，包含：

- 向量相似度搜尋
- CrossEncoder rerank
- Prompt 組裝
- Ollama API 測試

## 重要資料檔

Excel 規格資料：

- `data/HIWIN_Final_Data_V1.xlsx`
- `data/PMI_Optimized_Core_v2.xlsx`
- `data/FANUC_Motor_Specs_Direct.xlsx`

向量資料：

- `code/UI_test/LLM code/vector_data/*_final_chunks.npz`

規格圖片：

- `code/UI_test/characteristics_curves_and_data_sheet/page_*.png`

除非任務明確要求，不得修改、刪除或重新產生上述資料檔。

## 路徑管理規範

- 新增或修改 UI 測試區資料路徑時，優先集中在 `code/UI_test/ui_paths.py`。
- 避免在多個檔案中新增硬編碼絕對路徑。
- `Formula_set_lookup.py` 目前仍有絕對路徑；若要重構，需逐步改為相對路徑並驗證所有計算流程。
- 不得因為路徑錯誤而直接搬移或覆蓋資料檔。

## RAG 維護規範

若修改以下內容：

- `code/UI_test/llm_rag_service.py`
- `code/UI_test/LLM code/*`
- 向量資料庫功能
- RAG 查詢流程

禁止只修改 Prompt。必須同時檢查：

1. Query
2. Retrieval
3. Similarity Score
4. Top K
5. Context
6. Prompt
7. LLM Response

若修改 RAG 行為，完成後需回報檢索邏輯、召回內容、模型輸出與可能風險。

## 型號查詢規範

型號查詢優先使用 Exact Match。

例如查詢：

- `HG-KR23`
- `HG-KR43`
- `HG-KR73`

應避免 `HG-KR23` 召回 `HG-KR43` 或 `HG-KR73` 等錯誤結果。若無 Exact Match，再進行更寬鬆的相似查詢，並需清楚標示結果不是精確匹配。

## Query Router 規範

以下輸入不應進入 RAG：

- `HI`
- `Hello`
- `哈囉`
- `test`
- `測試`

這類輸入應直接回覆招呼語或簡短測試回應。只有技術查詢、規格查詢、型號查詢、選型問題或與進給系統相關的問題才允許進入 RAG。

## Git 安全規範

禁止執行以下指令，除非使用者明確要求：

```bash
git reset --hard
git checkout .
git clean -fd
git restore .
```

不得覆蓋使用者尚未提交的工作內容。若工作區已有未提交變更，應先檢查 `git status --short`，只修改本次任務需要的檔案。

## 開始工作前檢查清單

每次開始修改前，請先完成並向使用者說明：

1. 已閱讀 `AGENTS.md`
2. 本次任務理解
3. 預計修改檔案
4. 修改原因
5. 是否影響：
   - Streamlit UI
   - RAG
   - 規格推薦
   - 圖片配對
   - 向量資料庫
6. 測試方式

## 完成工作後回報格式

完成後請回報完整工作報告，不得只回覆「已完成」或只提供簡短摘要。若某項無內容，仍需明確寫「無」或說明原因。

### 修改檔案

列出本次實際修改的檔案。

### 修改內容

簡述每個檔案的變更重點。

### 執行流程變更

說明本次修改後的主要執行流程、資料流或使用者操作流程是否改變；若無變更，請寫「無」。

### 測試結果

列出已執行的測試與結果。若未執行，需說明原因。

### Debug 資訊

列出本次排查、trace、log、關鍵指標或其他有助於後續追蹤的資訊；若無，請寫「無」。

### 可能風險

說明已知風險、限制或未覆蓋情境。

### 後續建議

提出可選的下一步改善，不得假設使用者同意立即執行。

### git status 摘要

回報 `git status --short` 的重點摘要，說明本次相關變更與既有未提交變更；不得隱瞞工作區已有的其他變更。

## 預設假設

- `code/UI_test` 是目前主要開發區。
- `AGENTS.md` 位於專案根目錄。
- 後續 Agent 進入專案時應優先閱讀本文件。
- Streamlit 預設固定使用 `localhost:8888`。
- 其他資料夾預設視為參考資料、歷史流程或處理產物。
