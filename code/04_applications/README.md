# 04_applications - LLM 應用 & 服務

此階段集成前面的所有流程，實現 RAG（檢索增強生成）系統，提供智能查詢與回答功能。

## 📁 目錄結構

```
04_applications/
├── notebooks/           ← LLM 整合與應用探索
│   └── LLM串接工程.ipynb
├── scripts/             ← 生產環境應用服務
│   └── app_simple.py
└── README.md
```

## 🎯 使用流程

### LLM 整合探索

**LLM串接工程.ipynb**
- 連接 LLM API（OpenAI / 本地模型）
- 實現 RAG 邏輯
  - 查詢向量資料庫
  - 檢索相關文檔
  - 提供上下文給 LLM
- 提示詞工程優化
- 測試不同查詢場景

### 生產應用

**app_simple.py**
- 簡單的 Web 或 CLI 應用
- 使用者與系統互動介面
- 查詢、檢索、回答完整流程

## 🔗 系統架構

```
使用者查詢
    ↓
嵌入查詢文本
    ↓
向量資料庫搜尋 (top-k 相關文檔)
    ↓
格式化上下文
    ↓
送入 LLM 模型
    ↓
生成回答
    ↓
返回結果給使用者
```

## 🤖 LLM 模型選擇

### 雲端 API

| 模型 | 提供者 | 特點 | 成本 |
|------|--------|------|------|
| gpt-4 | OpenAI | 智能、可靠 | 較高 |
| gpt-3.5-turbo | OpenAI | 平衡效能 | 低 |
| claude-3 | Anthropic | 上下文大 | 中等 |

### 本地模型

| 模型 | 參數 | 優勢 | 要求 |
|------|------|------|------|
| Llama 2 | 7B-70B | 開源、可控 | GPU 或 CPU |
| Qwen | 7B-72B | 中文優化 | 中等 GPU |
| Mistral | 7B | 快速、輕量 | 低資源 |

## 📋 RAG 工作流

### 1. 查詢處理

```python
query = "上銀螺桿的承載能力如何計算?"

# 嵌入查詢
query_embedding = embedding_model.encode(query)

# 搜尋相關文檔
relevant_docs = vector_db.search(
    query_embedding,
    top_k=5,
    filter={"catalog": "HIWIN"}
)
```

### 2. 上下文格式化

```python
context = "\n\n".join([
    f"【文檔 {i+1}】\n來源：{doc['metadata']['page']}\n內容：{doc['text']}"
    for i, doc in enumerate(relevant_docs)
])
```

### 3. 提示詞組裝

```python
prompt = f"""基於以下技術文檔，回答用戶的問題。

【參考文檔】
{context}

【使用者問題】
{query}

【要求】
- 直接引用文檔中的數據
- 如果文檔中沒有相關資訊，明確說明
- 提供精確的技術規格與計算過程
"""
```

### 4. LLM 推理

```python
response = llm.generate(
    prompt,
    max_tokens=500,
    temperature=0.3  # 降低溫度提高確定性
)
```

## 💬 提示詞工程

### 系統提示

```
你是工業機械型錄的技術助手。
你的職責是基於提供的技術文檔回答用戶的詳細問題。
重點關注：規格、性能、計算方法、應用場景。
```

### 查詢範本

```
關於 [產品名稱]：
- 規格查詢：「HIWIN 上銀 DFS2505 的最大轉速?」
- 性能計算：「如何計算螺桿的負載承載力?」
- 應用建議：「哪個型號螺桿適合高速應用?」
```

## 🎛️ 應用配置

### 應用設定

```python
CONFIG = {
    "llm_model": "gpt-3.5-turbo",
    "embedding_model": "text-embedding-3-small",
    "vector_db_path": "../databases/hiwin_vector_db",
    "max_context_docs": 5,
    "temperature": 0.3,
    "max_tokens": 500,
}
```

### 搜尋策略

```python
# 混合搜尋（向量 + 關鍵詞）
results = hybrid_search(
    query=query,
    vector_weight=0.7,
    keyword_weight=0.3,
    filters={"catalog": "HIWIN"}
)
```

## 📈 性能優化

### 快取機制

```python
# 快取常見查詢結果
cache = {}
if query in cache:
    return cache[query]  # 直接返回
else:
    result = rag_pipeline(query)
    cache[query] = result
```

### 批量處理

```python
# 批量嵌入多個查詢
queries = [...many queries...]
embeddings = batch_encode(queries, batch_size=32)
```

### 索引最佳化

```python
# 預先建立篩選索引
vector_db.create_filter_index(
    field="catalog",
    values=["HIWIN", "PMI", "FANUC"]
)
```

## 🔧 故障排查

### LLM 回答不準確
- 增加檢索的文檔數量
- 改進提示詞設計
- 驗證向量品質

### 搜尋結果相關性低
- 檢查嵌入模型品質
- 調整搜尋參數
- 考慮使用混合搜尋

### 回應延遲高
- 啟用結果快取
- 使用更快的嵌入模型
- 優化資料庫查詢

### Token 成本高
- 使用更便宜的模型
- 優化上下文長度
- 實現智能快取

## 📊 評估指標

| 指標 | 目標 | 測量方法 |
|------|------|---------|
| 準確性 | > 80% | 人工評估 |
| 延遲 | < 2s | 計時測試 |
| 相關性 | > 0.7 | Cosine 相似度 |
| 成本 | 可控 | Token 統計 |

## 📝 推薦流程

1. **本地測試**
   - 在 notebook 中測試完整流程
   - 微調提示詞
   - 驗證回答品質

2. **建立應用**
   - 開發簡單 CLI 或 Web 介面
   - 集成所有組件
   - 進行端對端測試

3. **部署與監控**
   - 部署到生產環境
   - 監控性能指標
   - 收集使用者反饋

4. **持續改進**
   - 分析常見查詢
   - 優化提示詞
   - 更新文檔資料庫

## 📋 檢查清單

- [ ] LLM API 連接正常
- [ ] 向量嵌入功能正常
- [ ] 資料庫查詢正常
- [ ] 提示詞已測試
- [ ] 應用介面已完成
- [ ] 端對端流程已驗證
- [ ] 性能指標達標
