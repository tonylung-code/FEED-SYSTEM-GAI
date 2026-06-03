import numpy as np
import os
from pathlib import Path
from sentence_transformers import SentenceTransformer,CrossEncoder
import requests
from sklearn.metrics.pairwise import cosine_similarity

# 初始化模型
model = SentenceTransformer('BAAI/bge-m3')
model_reranking = CrossEncoder('BAAI/bge-reranker-v2-m3')

# ========= 手冊圖片查詢 =========
# 查詢圖片向量
def search_similar_content(query, npz_path):
    data = np.load(npz_path, allow_pickle=True)
    vectors = data['vectors']
    units = data['units'].tolist()
    
    query_vector = model.encode([query], normalize_embeddings=True)[0]
    similarities = np.dot(vectors, query_vector)
    # 查詢前5相似的內容
    top_k=5
    top_indices = np.argsort(similarities)[::-1][:top_k]
    results = [(units[idx], float(similarities[idx])) for idx in top_indices]
    
    # 回傳圖片路徑
    name_without_ext = Path(npz_path).stem
    return [
        os.path.join(name_without_ext, units[idx][0], f"page_{units[idx][1]}.png").replace('\\', '/')
        for idx in top_indices
    ]

# ======= 手冊查詢生成回覆 =======
# 全手冊查詢
def rerank_recall_results(contents, query, top_k=3):
    pairs = [[query, content] for content in contents]
    
    # 計算 Relevance Scores
    scores = model_reranking.predict(pairs)
    
    # 根據分數排序並選取前 top_k
    scored_chunks = list(zip(contents, scores))
    scored_chunks.sort(key=lambda x: x[1], reverse=True)
    top_chunks = [chunk for chunk, score in scored_chunks[:top_k]]
    
    return top_chunks

# 搜尋手冊相關資料
def simple_search(query, embeddings_name):
    if embeddings_name == 'All':
        # 模型表
        embeddings=['FANUC','HIWIN','PMI']
        result=[]
        for item in embeddings:
            search = simple_search(query,item)
            result.extend(search)
        recall_results=rerank_recall_results(result,query)
        return recall_results
    else:
        # 加載向量模型檔
        embeddings_path = f'vector_data/{embeddings_name}_final_chunks.npz'
        data = np.load(embeddings_path, allow_pickle=True)
        embeddings = data['embeddings']
        texts = data['texts']
        
        # 問題轉向量
        query_vec = model.encode([query], normalize_embeddings=True)
        
        # 計算相似度
        similarities = cosine_similarity(query_vec, embeddings)[0]
        
        # 計算前三高的元素
        top_k=3
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # 返回结果
        results = [texts[idx] for idx in top_indices]
        
        return results

# 組合使用者問題與資料問題
def optimize_prompt(question, context,calc):
    # 1. 限制上下文長度（避免過長導致回應慢）
    max_context_length= 2000 # 設定限制長度為2000
    if len(context) > max_context_length:
        context = context[:max_context_length] + "..."

    # 2. 結構化的提示詞模板
    myPrompt = f"""
        <Role>你是一位精通機械傳動與 CNC 系統的資深工程師。</Role>
        <Context>
        使用者目前計算出的建議型號：
        - 品牌系列：{calc.get('brand')} {calc.get('series')}
        - 型號：{calc.get('model')}
        - 物理參數：直徑 {calc.get('dia')}mm / 導程 {calc.get('lead')}mm
        - 動負荷：{calc.get('dynamic_load')} kgf
        </Context>
        <Reference_Data>
        {context}
        </Reference_Data>
        <User_Query>
        {question}
        </User_Query>
        <Instruction>
        1. 請分析建議型號是否滿足使用者需求。
        2. 參考 Reference_Data 中的技術細節（如安裝注意、潤滑要求或剛性表現）。
        3. 若涉及到 FANUC 電機匹配，請結合資料庫中的 Motor 資訊。
        4. 請使用「繁體中文」回答，保持專業工程師口吻，必要時以條列式說明。
        </Instruction>
    """
    return myPrompt

# 模型生成回覆
def query_ollama(question, answer,calc):
    headers = { "Content-Type": "application/json" }
    data = {
        "model": "llama3.2:latest", # 模型可以再調整
        "prompt": optimize_prompt(question, answer,calc),
        "temperature": 0.3,      # 降低隨機性，提高準確性
        "top_p": 0.9,            # 提高核心取樣，保持多樣性
        "max_tokens": 512,       # 限制輸出長度，加快回應
        "num_predict": 512,      # Ollama 專用參數
        "repeat_penalty": 1.1,   # 避免重複
        "timeout": 60,
        "stream": False
    }
    
    try:
        response = requests.post("http://localhost:11434/api/generate", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["response"] 
    except Exception as e:
        return f"請求出錯: {str(e)}"

# 使用示例
if __name__ == "__main__":
    # (1)圖片查詢(回傳圖檔路徑)
    question='40/3000HV FAN-D'
    results = search_similar_content(question,"B65542EN_01_ai-D伺服馬達仕樣.npz")
    print(results)

    # (2)查詢手冊問題生成(回傳模型回覆)
    # 測試的計算數據
    calc_result = {
    "brand": "HIWIN",
    "series": "FDC",
    "model": "40-12K5",
    "dia": 40.0,
    "lead": 12.0,
    "dynamic_load": 7430
    }
    # 向量模型名稱
    vector_name = ['FANUC','HIWIN','PMI','All']
    # All表示全選
    # 問題
    question='請問本手冊的內容可以複製嗎?'

    # 手冊問題生成回覆
    search = simple_search(question,'FANUC')
    myPrompt = query_ollama(question,search,calc_result)
    print(f'模型回覆: {myPrompt}')
