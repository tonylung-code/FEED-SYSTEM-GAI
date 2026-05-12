import chromadb
from pathlib import Path
import chromadb
from pathlib import Path
from collections import Counter
import ollama
import re

def find_db_path(anchor_name="FEED-SYSTEM-GAI"):
    """自動尋找專案根目錄錨點"""
    # 從目前執行腳本的檔案位置開始向上溯源
    current_path = Path(__file__).resolve()
    
    for parent in [current_path, *current_path.parents]:
        if parent.name == anchor_name:
            return parent/ "databases" / "hiwin_vector_db"
            
    # 若找不到錨點（例如資料夾改名），則退而求其次尋找特徵資料夾
    for parent in [current_path, *current_path.parents]:
        if (parent / "databases").exists():
            return parent
            
    raise FileNotFoundError(f"無法定位專案根目錄，請確保資料夾名稱包含 {anchor_name}")

def data_type_statistics():
    DB_PATH = find_db_path()
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collections = client.list_collections()
    col = client.get_collection("screw_specs")
    data = col.get(include=["metadatas"])

    triples = Counter(
        (
            m.get("brand", ""),
            m.get("category", ""),
            m.get("data_type", "")
        )
        for m in data["metadatas"]
    )

    print("--- 資料類型統計 ---")
    for key, count in sorted(triples.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {count}")

# 設定資料庫路徑
DB_PATH = find_db_path()
client = chromadb.PersistentClient(path=str(DB_PATH))
collection = client.get_collection("screw_specs")

def get_expert_advice_gemma(user_query, calc_result, use_rag=True):
    """
    針對 Sigma CNC 機械研發場景優化的 RAG 邏輯
    """
    print(f"成功連接向量資料庫：{DB_PATH}")
    print(f"Collection: screw_specs，共 {collection.count()} 筆資料")

    def keyword_search(query, data_type=None, n_results=3):
        """不依賴外部 embedding 模型的檢索 fallback。"""
        where = {"data_type": data_type} if data_type else None
        data = collection.get(where=where, include=["documents", "metadatas"])
        tokens = [t.lower() for t in re.findall(r"[A-Za-z0-9\u4e00-\u9fff]+", query)]
        scored = []

        for doc, meta in zip(data["documents"], data["metadatas"]):
            meta_text = " ".join(str(v) for v in meta.values())
            haystack = f"{doc} {meta_text}".lower()
            score = sum(haystack.count(token) for token in tokens)
            scored.append((score, doc, meta))

        scored.sort(key=lambda item: item[0], reverse=True)
        top = scored[:n_results]
        return {
            "documents": [[doc for _, doc, _ in top]],
            "metadatas": [[meta for _, _, meta in top]],
        }
    # --- 1. 精準檢索策略 ---
    # 同時檢索規格 (Specs) 與 手冊 (Manual)，並加入品牌過濾 (可選)
    def smart_query(query, data_type, n=2):
        return keyword_search(query, data_type=data_type, n_results=n)

    if use_rag:
        try:
            spec_res = smart_query(user_query, "Specification", n=3)
            manual_res = smart_query(user_query, "Manual", n=2)
            
            rag_context = f"""
【技術規格參考】:
{" ".join(spec_res['documents'][0])}

【手冊操作細節】:
{" ".join(manual_res['documents'][0])}
        """
        except Exception as e:
            rag_context = f"檢索異常: {e}"
    else:
        rag_context = "本次未啟用 RAG 檢索，僅根據目前計算結果回答。"

    # --- 2. 建立 Prompt (針對 Gemma 3 4B 優化) ---
    # Gemma 3 對 XML 標籤或結構化區塊反應極佳
    prompt = f"""
    <Role>你是一位精通機械傳動與 CNC 系統的資深工程師，服務於 Sigma CNC Technology。</Role>
    
    <Context>
    使用者目前計算出的建議型號：
    - 品牌系列：{calc_result.get('brand')} {calc_result.get('series')}
    - 型號：{calc_result.get('model')}
    - 物理參數：直徑 {calc_result.get('dia')}mm / 導程 {calc_result.get('lead')}mm
    - 動負荷：{calc_result.get('dynamic_load')} kgf
    </Context>

    <Reference_Data>
    {rag_context}
    </Reference_Data>

    <User_Query>
    {user_query}
    </User_Query>

    <Instruction>
    1. 請分析建議型號是否滿足使用者需求。
    2. 參考 Reference_Data 中的技術細節（如安裝注意、潤滑要求或剛性表現）。
    3. 若涉及到 FANUC 電機匹配，請結合資料庫中的 Motor 資訊。
    4. 請使用「繁體中文」回答，保持專業工程師口吻，必要時以條列式說明。
    </Instruction>
    """

    # --- 3. 執行生成 ---
    try:
        response = ollama.generate(
            model='gemma3n:e4b',
            prompt=prompt,
            options={
                "temperature": 0.3, # 保持技術準確性
                "num_ctx": 4096     # 確保 Context 夠大處理 RAG 內容
            }
        )
        return response['response']
    except Exception as e:
        return f"Ollama Error: {e}"


calc_result = {
    "brand": "HIWIN",
    "series": "FDC",
    "model": "40-12K5",
    "dia": 40.0,
    "lead": 12.0,
    "dynamic_load": 7430
}

# 測試提問
# user_query = "螺帽直徑跟長度空間有限，是否有其他型號建議"

# print("正在調用 gemma3n:e4b 進行分析...\n")
# result = get_expert_advice_gemma(user_query, calc_result, use_rag=True)
# print("\n--- 專家建議結果 ---")
# print(result) # 使用 Markdown 讓回答看起來更漂亮

import ollama

def get_active_model():
    try:
        # 取得模型回應物件
        response = ollama.list()
        
        # 修正點：使用物件屬性 .model 獲取完整名稱 (如 'gemma3n:e4b')
        model_names = [m.model for m in response.models]
        
        if not model_names:
            print("❌ Ollama 服務正常，但未偵測到任何已下載模型。")
            return None
        
        # 優先尋找包含 gemma 的模型，否則取第一個
        target = next((m for m in model_names if "gemma" in m.lower()), model_names[0])
        return target
    except Exception as e:
        print(f"❌ 無法連接 Ollama 服務或解析失敗: {e}")
        return None


# 對話視窗
def start_chat():
    print(f"\n{'='*50}")
    print(f"🚀 Feed_system 研發專家系統已啟動")
    print(f"📍 資料庫路徑: {DB_PATH}")
    print(f"🤖 模型: {get_active_model()}")
    print(f"👉 輸入 'exit' 或 'quit' 結束對話")
    print(f"{'='*50}\n")

    # 模擬或從你的 calc_result 獲取
    context_calc = calc_result

    while True:
        try:
            user_input = input("\n👤 工程師提問: ").strip()
            
            if not user_input:
                continue
            if user_input.lower() in ['exit', 'quit']:
                print("👋 系統關閉，研發順利！")
                break

            print("\n🔍 正在檢索並生成建議...", end="\r")
            
            # 這裡調用你的專家建議邏輯，但改為直接在內部處理輸出
            # 為了讓互動更流暢，建議將 get_expert_advice_gemma 內的 ollama 呼叫改為 stream
            
            print("🤖 AI 工程師建議：")
            print("-" * 30)
            
            # --- 以下為整合後的流式輸出部分 ---
            # 重新封裝 Prompt 邏輯
            # (假設你保留原有的 rag_context 檢索代碼)
            
            # 執行流式生成
            stream = ollama.generate(
                model='gemma3n:e4b',  # 請確認你的型號名稱
                prompt=f"使用者提問：{user_input}\n背景：{context_calc}\n請用繁體中文回答。",
                stream=True,
                options={"temperature": 0.3}
            )

            for chunk in stream:
                content = chunk['response']
                print(content, end='', flush=True)
            
            print("\n" + "-" * 30)

        except KeyboardInterrupt:
            print("\n操作已取消。")
            break
        except Exception as e:
            print(f"\n❌ 發生錯誤: {e}")

if __name__ == "__main__":
    start_chat()