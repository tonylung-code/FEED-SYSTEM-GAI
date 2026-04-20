# 工業型錄 AI 提取與 RAG 系統

一個完整的工業機械型錄資訊提取、處理、向量化與 AI 查詢系統。

## 🎯 專案目標

從 PDF 型錄（上銀、銀泰、FANUC）中自動提取文字與規格資訊，建立向量資料庫，
結合大語言模型（LLM）實現智能查詢與回答系統。

## 📁 專案結構

```
code/
├── 01_extraction/              ← PDF 文字與表格擷取
│   ├── notebooks/              ← 互動式探索
│   ├── scripts/                ← 自動化指令碼
│   └── README.md
│
├── 02_processing/              ← 資料清理與參數處理
│   ├── notebooks/              ← 清理與轉換
│   ├── scripts/                ← 自動化處理
│   └── README.md
│
├── 03_embeddings/              ← 向量化與資料庫
│   ├── notebooks/              ← 嵌入與 ChromaDB
│   └── README.md
│
├── 04_applications/            ← LLM 應用
│   ├── notebooks/              ← RAG 系統設計
│   ├── scripts/                ← 生產應用
│   └── README.md
│
├── outputs/                    ← 中間結果與最終輸出
│   ├── *_final_chunks.json    ← 擷取的文本塊
│   ├── *_extraction_check.md  ← 擷取驗證結果
│   └── catalog_*.{json,md}    ← 型錄擷取結果
│
├── databases/                  ← 向量資料庫
│   └── hiwin_vector_db/       ← ChromaDB 實例
│
└── README.md                   ← 本檔案
```

## 🚀 快速開始

### 前置需求

```bash
# 已有虛擬環境
source venv/Scripts/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt
```

### 完整工作流

#### 1️⃣ 提取階段

```bash
cd code/01_extraction/scripts
python "文字說明內容擷取(上銀 銀泰 FUNAC) V2.py"

# 或使用 notebook 進行互動式探索
jupyter notebook ../notebooks/上銀型錄文字擷取.ipynb
```

**輸出**：`code/outputs/*.json` 與 `code/outputs/*.md`

#### 2️⃣ 處理階段

```bash
cd code/02_processing/notebooks
jupyter notebook 參數轉換公式.ipynb
# 執行資料清理與參數轉換
```

**輸出**：清理後的結構資料

#### 3️⃣ 嵌入階段

```bash
cd code/03_embeddings/notebooks
jupyter notebook chromadb資料庫處理與整合.ipynb
# 向量化並儲存到 ChromaDB
```

**輸出**：`code/databases/hiwin_vector_db/`

#### 4️⃣ 應用階段

```bash
cd code/04_applications/scripts
python app_simple.py

# 或執行 notebook 測試
jupyter notebook ../notebooks/LLM串接工程.ipynb
```

## 📊 關鍵檔案

### 文本擷取

| 檔案 | 用途 | 輸出 |
|------|------|------|
| 上銀型錄文字擷取.ipynb | 上銀滾珠螺桿擷取 | JSON + Markdown |
| 銀泰型錄文字擷取.ipynb | 銀泰螺桿擷取 | JSON + Markdown |
| 馬達資料處裡.ipynb | FANUC 規格表擷取 | Excel + CSV |

### 資料處理

| 檔案 | 用途 | 輸出 |
|------|------|------|
| 參數比對.ipynb | 參數映射對比 | CSV 對應表 |
| 參數轉換公式.ipynb | 計算與轉換 | 轉換函式庫 |

### 核心應用

| 檔案 | 用途 | 功能 |
|------|------|------|
| embeding 工程.ipynb | 向量化實驗 | 模型測試 |
| chromadb 整合.ipynb | 向量資料庫 | 搜尋驗證 |
| LLM 串接工程.ipynb | RAG 系統 | 查詢與回答 |
| app_simple.py | 應用服務 | Web/CLI 介面 |

## 🔧 組態設定

### 環境變數

```bash
# .env 檔案
OPENAI_API_KEY=your_api_key_here
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-3.5-turbo
VECTOR_DB_PATH=./databases/hiwin_vector_db
```

### 主要參數

```python
# 擷取配置
CHUNK_SIZE = 600        # 文本塊大小
OVERLAP = 100           # 塊重疊

# 嵌入配置
EMBEDDING_DIM = 1536    # 向量維度
BATCH_SIZE = 100        # 批處理大小

# LLM 配置
TEMPERATURE = 0.3       # 回答確定性
MAX_TOKENS = 500        # 最大生成長度
MAX_CONTEXT_DOCS = 5    # 檢索文檔數
```

## 📈 工作流程圖

```
PDF 型錄
   ↓
[01] 文字擷取 ──→ Raw JSON/Markdown
   ↓
[02] 資料清理 ──→ 結構化資料 (CSV/Excel)
   ↓
[03] 向量化 ──→ ChromaDB (向量資料庫)
   ↓
[04] LLM 應用 ──→ RAG 系統
   ↓
使用者查詢 ──→ 智能回答
```

## 🎓 使用指南

### 對於開發者

1. **探索現有邏輯**
   - 閱讀各階段的 README
   - 執行 notebook 了解工作流

2. **修改與優化**
   - 調整過濾條件（`01_extraction`）
   - 改進提示詞（`04_applications`）
   - 優化模型配置（`03_embeddings`）

3. **擴展功能**
   - 新增資料來源
   - 實現新的轉換公式
   - 開發 API 端點

### 對於使用者

1. **查詢示例**
   ```
   「上銀螺桿的最大轉速是多少?」
   「如何計算螺桿的承載能力?」
   「哪個型號螺桿適合高速應用?」
   ```

2. **檢查結果**
   - 驗證引用的文檔來源
   - 檢查提供的規格數據
   - 確認計算方法是否正確

## 🔍 故障排查

### 常見問題

| 問題 | 解決方案 |
|------|---------|
| 找不到 PDF | 檢查 `../data/` 路徑 |
| 擷取結果過少 | 調整頁面過濾閾值 |
| 搜尋不準確 | 驗證嵌入模型品質 |
| LLM 回答不好 | 改進提示詞設計 |

### 調試步驟

1. 查看各階段的 README
2. 執行相應 notebook 檢查輸出
3. 調整參數重新運行
4. 檢查中間輸出檔案（`outputs/`）

## 📚 相關資源

- [ChromaDB 文檔](https://docs.trychroma.com/)
- [OpenAI API 指南](https://platform.openai.com/docs/)
- [Sentence Transformers](https://www.sbert.net/)
- [PyMuPDF 文檔](https://pymupdf.readthedocs.io/)

## 📝 維護與更新

### 資料更新

1. 新增 PDF 型錄到 `../data/`
2. 更新 `01_extraction/scripts` 中的 `CATALOGS`
3. 重新執行擷取流程
4. 更新向量資料庫

### 模型更新

- 定期測試新的嵌入模型
- 評估 LLM 性能
- 監控成本與延遲

## 🤝 貢獻指南

- 改進提示詞工程
- 優化搜尋演算法
- 新增功能或整合
- 改進文檔

## 📞 支援

遇到問題或有建議？請查閱各階段的 README 或聯絡開發團隊。

---

**最後更新**：2026-04-20  
**版本**：1.0
