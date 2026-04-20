# 01_extraction - 文字與表格擷取

此階段負責從 PDF 型錄中擷取原始文字和表格資料。

## 📁 目錄結構

```
01_extraction/
├── notebooks/           ← 互動式擷取探索
│   ├── 上銀型錄文字擷取.ipynb
│   ├── 銀泰型錄文字擷取.ipynb
│   └── 馬達資料處裡.ipynb
├── scripts/             ← 自動化擷取指令碼
│   ├── 文字說明內容擷取(上銀 銀泰 FUNAC).py
│   └── 文字說明內容擷取(上銀 銀泰 FUNAC) V2.py
└── README.md
```

## 🎯 使用流程

### 使用 Notebooks（適合探索與調試）

1. **上銀型錄文字擷取.ipynb**
   - 從上銀滾珠螺桿 PDF 擷取文字
   - 包含初步清理與段落過濾
   - 輸出：markdown 與 JSON 格式的擷取結果

2. **銀泰型錄文字擷取.ipynb**
   - 從銀泰螺桿 PDF 擷取文字
   - 相同清理流程
   - 輸出：markdown 與 JSON 格式的擷取結果

3. **馬達資料處裡.ipynb**
   - 從 FANUC 馬達 PDF 提取表格資料
   - 重點：型號、規格、性能指標
   - 輸出：Excel 格式的規格表

### 使用 Scripts（適合批量自動化）

```bash
# 執行完整的文字與公式擷取
cd code/01_extraction/scripts
python "文字說明內容擷取(上銀 銀泰 FUNAC) V2.py"

# 輸出位置：code/outputs/
```

## 📊 擷取結果

### 輸出檔案類型

- **JSON**：結構化資料，方便後續程式處理
- **Markdown**：人工檢查與驗證的可讀格式
- **Excel**：表格規格的展示形式

### 資料內容

- **文字**：產品說明、技術規格、安裝指南
- **公式**：計算公式、性能計算式
- **表格**：型號對照、參數規格

## ⚙️ 關鍵參數

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `chunk_size` | 文字區塊大小 | 600-1000 字元 |
| `overlap` | 區塊重疊長度 | 100 字元 |
| `min_chunk_size` | 最小區塊長度 | 100 字元 |

## 🔧 故障排查

### 找不到 PDF 檔案
- 確認 `CATALOGS` 中的路徑正確
- 檔案應在 `../../data/` 目錄中

### 擷取結果過少
- 檢查頁面過濾條件（是否過度跳過有用頁面）
- 調整 `is_table_heavy_page()` 中的閾值

### 嵌入表格或雜訊
- 增強 `is_description_block()` 的過濾邏輯
- 手動調整 `data_density` 或 `text_ratio` 閾值

## 📝 備註

- 文字擷取後的結果存放在 `code/outputs/`
- 各個 notebook 的中間檢查結果也會在同層產生（*.md、*.json）
- 建議先用 notebook 探索，理解邏輯後再用 script 批量處理
