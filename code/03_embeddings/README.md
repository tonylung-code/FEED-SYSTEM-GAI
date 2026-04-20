# 03_embeddings - 向量化 & 嵌入工程

此階段負責將文字資料轉換為向量表示，並存儲到向量資料庫供 RAG 系統使用。

## 📁 目錄結構

```
03_embeddings/
├── notebooks/           ← 嵌入與向量化探索
│   ├── embeding 工程.ipynb
│   └── chromadb資料庫處理與整合.ipynb
└── README.md
```

## 🎯 使用流程

### 嵌入向量化

**embeding 工程.ipynb**
- 文字分詞與預處理
- 選擇嵌入模型（OpenAI / 本地模型）
- 生成高維向量表示
- 維度縮減（可選）
- 驗證向量品質

### 向量資料庫整合

**chromadb資料庫處理與整合.ipynb**
- 連接 ChromaDB 向量資料庫
- 批量匯入嵌入向量
- 建立集合與索引
- 相似度搜尋測試
- 性能最佳化

## 🔗 資料流

```
清理後的文字 (JSON)
    ↓
分詞與預處理
    ↓
選擇嵌入模型
    ↓
向量化 (1536 維或其他)
    ↓
儲存到 ChromaDB
    ↓
建立搜尋索引
```

## 🧠 嵌入模型選擇

### 雲端服務
| 模型 | 提供者 | 維度 | 優勢 | 成本 |
|------|--------|------|------|------|
| text-embedding-3-small | OpenAI | 1536 | 高品質 | 按次計費 |
| text-embedding-3-large | OpenAI | 3072 | 更精細 | 較高 |

### 本地模型
| 模型 | 維度 | 優勢 | 缺點 |
|------|------|------|------|
| sentence-transformers | 384-768 | 離線、低成本 | 品質略低 |
| m2-bert-multilingual | 768 | 多語言支援 | 需 GPU 加速 |

## 💾 ChromaDB 設定

### 連接方式

```python
import chromadb

# 本地持久化模式
client = chromadb.Client(
    settings=chromadb.config.Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./databases/hiwin_vector_db",
        anonymized_telemetry=False
    )
)

# 建立集合
collection = client.get_or_create_collection(
    name="product_catalogs",
    metadata={"hnsw:space": "cosine"}
)
```

### 批量匯入

```python
# 新增文件與嵌入
collection.add(
    ids=[...],           # 唯一識別碼
    embeddings=[...],    # 向量列表
    documents=[...],     # 原始文字
    metadatas=[...]      # 元資料 (來源、頁碼等)
)
```

## 🔍 相似度搜尋

### 基本查詢

```python
# 查詢相似文檔
results = collection.query(
    query_embeddings=[[...]],
    n_results=5,
    where={"catalog": "HIWIN"}  # 可選過濾
)
```

### 查詢結果結構

```python
{
    "ids": ["doc_1", "doc_2", ...],
    "documents": ["文本內容", ...],
    "metadatas": [{"page": 10, "catalog": "HIWIN"}, ...],
    "distances": [0.1, 0.2, ...]  # 距離越小相似度越高
}
```

## ⚙️ 最佳化配置

### 嵌入最佳化

```python
# 分批處理大量文件（避免記憶體溢出）
BATCH_SIZE = 100

# 模型快取
device = "cuda" if torch.cuda.is_available() else "cpu"
```

### 資料庫最佳化

```python
# HNSW 參數
{
    "hnsw:space": "cosine",      # 餘弦距離
    "hnsw:M": 16,               # 層間連結數
    "hnsw:ef_construction": 200  # 構建時的搜尋範圍
}

# 定期維護
collection.delete(where={...})  # 刪除舊資料
collection.compact()            # 壓縮空間
```

## 📊 性能指標

### 向量品質檢查

| 指標 | 目標 | 說明 |
|------|------|------|
| 平均相似度 | > 0.7 | 同類文檔相似度 |
| 離群度 | < 0.1 | 向量分佈異常值 |
| 搜尋延遲 | < 100ms | 單次查詢時間 |

### 資料庫統計

```python
# 查詢集合統計
stats = collection.count()
print(f"儲存文檔數: {stats}")

# 查詢記憶體使用
import os
size = os.path.getsize("./databases/hiwin_vector_db")
print(f"資料庫大小: {size / 1024 / 1024:.2f} MB")
```

## 🔧 故障排查

### 記憶體不足
- 減少 `BATCH_SIZE`
- 使用模型量化
- 在 GPU 上執行

### 查詢速度慢
- 調整 HNSW 參數
- 增加 `ef_construction` 值
- 考慮使用 GPU 加速

### 向量品質差
- 檢查文字預處理
- 嘗試不同嵌入模型
- 驗證資料清理品質

## 📝 推薦流程

1. **測試嵌入模型**
   - 在小樣本上測試
   - 比較不同模型效果
   - 選定最佳方案

2. **建立向量資料庫**
   - 設定 ChromaDB
   - 匯入部分資料測試
   - 驗證搜尋效果

3. **批量匯入與最佳化**
   - 全量匯入資料
   - 調整資料庫參數
   - 建立索引

4. **集成到 RAG 系統**
   - 連接 LLM 應用
   - 測試端對端流程
   - 監控搜尋品質

## 📋 檢查清單

- [ ] 選定嵌入模型
- [ ] 測試嵌入品質
- [ ] ChromaDB 連接正常
- [ ] 所有文檔已匯入
- [ ] 搜尋功能正常
- [ ] 性能指標達標
