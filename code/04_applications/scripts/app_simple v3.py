import streamlit as st
import pandas as pd
import math

try:
    import chromadb
    import ollama
    from chromadb.config import Settings
    RAG_AVAILABLE = True
except ImportError:
    RAG_AVAILABLE = False

# --- [1. 頁面設定] ---
st.set_page_config(page_title="HIWIN 智慧選型系統", layout="wide")

# --- [2. 自定義 CSS] ---
st.markdown("""
    <style>
    .recommendation-box {
        background-color: #1E3A8A;
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    .recommendation-box h4 { color: white !important; margin: 0; }

    .big-font {
        font-size: 26px !important;
        font-weight: bold;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [3. 資料載入與快取] ---
@st.cache_data
def load_screw_data():
    hiwin_df = pd.read_excel("data/HIWIN_Final_Data_V1.xlsx", engine='openpyxl')
    pmi_df = pd.read_excel("PMI_Final_Data_V3.xlsx", engine='openpyxl')
    return hiwin_df, pmi_df

@st.cache_data
def load_motor_data():
    fanuc_df = pd.read_excel("data/FANUC_Specs.xlsx", engine='openpyxl')
    return fanuc_df

# 載入資料
hiwin_screws, pmi_screws = load_screw_data()
fanuc_motors = load_motor_data()

# ChromaDB 設定
if RAG_AVAILABLE:
    chroma_client = chromadb.PersistentClient(path="databases/hiwin_vector_db", settings=Settings(anonymized_telemetry=False))
    collection = chroma_client.get_or_create_collection(name="screw_specs")
    
    # 初始化 collection 如果為空
    if collection.count() == 0:
        # 從型錄文本擷取 JSON 加載數據
        import json
        try:
            with open("outputs/catalog_text_formula_extraction_20260420_160730.json", "r", encoding="utf-8") as f:
                catalog_data = json.load(f)
            
            documents = [item["content"] for item in catalog_data if "content" in item]
            ids = [f"chunk_{i}" for i in range(len(documents))]
            metadatas = [{"source": "catalog_extraction", "chunk_id": i} for i in range(len(documents))]
            
            collection.add(
                documents=documents,
                ids=ids,
                metadatas=metadatas
            )
        except FileNotFoundError:
            # 如果文件不存在，使用預設數據
            default_docs = [
                "FANUC SERVO MOTOR αi-D series 規格說明",
                "HIWIN 滾珠螺桿動負荷計算公式",
                "PMI 銀泰螺桿技術參數",
                "伺服馬達扭矩計算方法"
            ]
            ids = [f"default_{i}" for i in range(len(default_docs))]
            metadatas = [{"source": "default", "chunk_id": i} for i in range(len(default_docs))]
            collection.add(
                documents=default_docs,
                ids=ids,
                metadatas=metadatas
            )
else:
    collection = None

# --- [4. 計算函數] ---
def calculate_lead(max_feed_rate, motor_max_speed, reduction_ratio=1):
    return max_feed_rate / (motor_max_speed * reduction_ratio)

def calculate_screw_max_speed(max_feed_rate, lead):
    return max_feed_rate / lead

def calculate_diameter_range(max_feed_rate, lead, length, load, cutting_force, gravity_axis_YN=True, cof=0.008, E=21000, f=[9.7, 15.1, 21.9, 3.4], n=[4.0, 2.0, 0.25]):
    # 臨界轉速估算直徑
    N_m = (max_feed_rate / lead) * 0.5
    dr_n = round((N_m * length**2 / f[2]) * 1e-7, 0)

    # 挫曲負荷估算直徑
    if gravity_axis_YN:
        p = (load + cutting_force) * 2
    else:
        p = (cutting_force + load * cof) * 2
    dr_p = round((p * 64 * length**2 / (n[0] * math.pi**3 * E))**(0.25), 0)

    dr_F = max(dr_n, dr_p)
    dr_DN = round(150000 / (max_feed_rate / lead), 0)

    diameters = [12, 14, 15, 16, 20, 25, 28, 32, 36, 40, 45, 50, 55, 63, 70, 80, 100]
    suitable = [d for d in diameters if dr_F <= d <= dr_DN]
    return suitable

def calculate_dynamic_load(load, cutting_force, preload_rate=0.05, gravity_axis_YN=True, cof=0.008):
    if gravity_axis_YN:
        p = load + cutting_force
    else:
        p = cutting_force + load * cof
    c = round(p / (3 * preload_rate), 0)
    return c

def calculate_motor_torque(lead, load, cutting_force, me=0.9, cof=0.008):
    T_t1 = (1 + cof) * lead * load / (2 * math.pi * me)
    T_t2 = abs((1 - cof) * lead * load / (2 * math.pi * me))
    T_t = round(max(T_t1, T_t2) * 9.8e-3, 2)

    T_c = round(cutting_force * lead * me / (2 * math.pi) * 9.8e-3, 2)

    T_rf = T_c + T_t
    return T_rf

def calculate_load_inertia(length, diameter_range, load, guide):
    # 參考參數轉換公式.ipynb 的 Motor_inertia_calculation
    proportion = 0.0078
    L = length  # mm
    g = 980  # cm/s²
    # 使用最大直徑計算螺桿慣量
    max_diameter = max(diameter_range) if diameter_range else 20
    Js = math.pi * proportion * (L * 0.1) * ((max_diameter * 0.1)**4) / (32 * g)  # kgf*cm*s**2
    
    W = load  # kgf
    hsp = guide * 0.1  # cm
    Jt = W / g * (hsp / 2 / math.pi)**2  # kgf*cm*s**2
    
    JL = round(Js + Jt, 4)  # kgf·cm·s²
    return JL

# --- [5. 推薦系統] ---
def recommend_screws(brand, lead, diameter_range, required_dynamic_load, safety_factor=1.2):
    if brand == "HIWIN":
        df = hiwin_screws
    elif brand == "PMI":
        df = pmi_screws
    else:
        return []

    filtered = df[
        (df['導程'] == lead) &
        (df['公稱 外徑'].isin(diameter_range)) &
        (df['動負荷 C (kfg)'] >= required_dynamic_load * safety_factor)
    ].sort_values('動負荷 C (kfg)', ascending=False).head(5)

    return filtered.to_dict('records')

def recommend_motors(required_torque, motor_max_speed, safety_factor=1.2):
    # FANUC data is itemized; find models with torque >= required
    torque_rows = fanuc_motors[fanuc_motors['Item'].str.contains('torque', case=False, na=False)]
    # Filter for Nm units only
    torque_rows = torque_rows[torque_rows['Unit'].str.strip() == 'Nm']
    
    # Simple filter: models where any torque value >= required
    qualified_data = torque_rows[torque_rows['Value'].astype(float) >= required_torque * safety_factor]
    # Assume speed is ok for now
    return [{'Model': row['Model'], 'Value': float(row['Value'])} for _, row in qualified_data.head(5).iterrows()]

# --- [6. RAG 聊天] ---
# 定義專業知識字典
SERIES_INFO = {
    "FDC": "雙螺帽設計，具備極高的軸向剛性與預壓穩定性，專為重負荷精密工具機設計。",
    "FSW": "小法蘭單螺帽設計，體積精簡，適合安裝空間受限的自動化設備。",
    "FSV": "標準單螺帽型，具備優異的傳動效率與流暢度，是自動化產業最泛用的標準件。",
    "RSI": "旋轉螺帽設計，適合絲槓固定、螺帽旋轉的機構，能有效抑制長行程下的振動。",
    "FSI": "內循環設計，螺帽外徑小，運轉安靜，適合小型精密設備。"
}

def rag_query(query, context=""):
    if not RAG_AVAILABLE or collection is None:
        return "RAG 功能不可用，請安裝 chromadb 和 ollama。"
    
    # 混合檢索架構：同時檢索技術手冊與產品規格
    rag_context = ""
    rag_status_msg = ""
    
    try:
        # 檢索型錄文本
        results = collection.query(query_texts=[query], n_results=5)
        docs = results['documents'][0] if results['documents'] else []
        rag_context = "\n【參考資料】：\n" + "\n".join(docs)
        rag_status_msg = "\n(系統提示：已完成檢索 - 參考型錄資料)\n"
    except Exception as e:
        rag_context = f"\n(系統提示：資料庫檢索失敗: {e})\n"
    
    # 準備計算結果上下文
    calc_context = f"""
    【目前計算參數】
    - 導程: {lead:.1f} mm
    - 動負荷需求: {required_dynamic_load} kgf
    - 扭矩需求: {required_motor_torque} N·m
    - 附載慣量: {load_inertia} kgf·cm·s²
    """
    
    # 組合最終 Prompt
    prompt = f"""
    你是一位專業的 HIWIN 技術支援工程師，請根據提供的【目前計算參數】與【參考資料】來回答提問。
    回答時請結合產品的物理特性與系列優點，請用繁體中文回答。
       
    當使用者詢問關於空間、尺寸或替代型號時，請優先參考「參考資料」進行對比。
    當使用者詢問關於安裝、保養或技術原理時，請參考「參考資料」。

    {calc_context}
    
    {rag_context}
    
    使用者提問：{query}
    
    請用繁體中文回答，語氣專業且誠懇，並儘可能引用具體參數。
    """
    
    # 呼叫 Ollama
    try:
        response = ollama.chat(model='gemma4-gpu', messages=[
            {'role': 'system', 'content': '你是一位精通機械工程與 CNC 零組件的繁體中文 AI 助理。請務必使用繁體中文（zh-TW）回答使用者的所有問題。請依據提供的上下文與計算結果，經過嚴謹的邏輯思考後，給出專業、精確的建議。'},
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content'] + rag_status_msg
    except Exception as e:
        return f"Ollama 錯誤: {str(e)}"

# --- [主頁面佈局] ---
# 四象限佈局
col1, col2 = st.columns([1, 1], gap="medium")
with col1:
    top_left = st.container()
    bottom_left = st.container()
with col2:
    top_right = st.container()
    bottom_right = st.container()

# 左上：輸入參數
with top_left:
    st.subheader("🛠️ 使用者設計條件")
    with st.container(border=True):
        mode = st.radio("選擇輸入模式", ["設計需求輸入", "零件規格輸入"], horizontal=True)
        
        # 預設值
        max_feed_rate = 48000.0
        motor_max_speed = 4000.0
        load = 775.0
        load_mass = 79.0
        cutting_force = 343.0
        screw_length = 924.0
        gravity_axis_YN = True
        safety_factor = 1.2
        screw_diameter = 40.0
        screw_lead = 12.0
        
        if mode == "設計需求輸入":
            c1, c2 = st.columns(2)
            with c1:
                max_feed_rate = st.number_input("最大進給速率 (mm/min)", value=48000.0, min_value=0.0)
                motor_max_speed = st.number_input("馬達最高轉速 (rpm)", value=4000.0, min_value=0.0)
                load = st.number_input("負載 (kgf)", value=775.0, min_value=0.0)
                load_mass = st.number_input("負載質量 (kg)", value=79.0, min_value=0.0)
            with c2:
                cutting_force = st.number_input("切削力 (kgf)", value=343.0, min_value=0.0)
                screw_length = st.number_input("螺桿長度 (mm)", value=924.0, min_value=0.0)
                gravity_axis_YN = st.checkbox("重力軸", value=True)
                safety_factor = st.slider("安全係數", min_value=1.0, max_value=2.0, value=1.2, step=0.1)
            
            # 計算
            lead = calculate_lead(max_feed_rate, motor_max_speed)
            screw_max_speed = calculate_screw_max_speed(max_feed_rate, lead)
            diameter_range = calculate_diameter_range(max_feed_rate, lead, screw_length, load, cutting_force, gravity_axis_YN)
            required_dynamic_load = calculate_dynamic_load(load, cutting_force, gravity_axis_YN=gravity_axis_YN)
            required_motor_torque = calculate_motor_torque(lead, load, cutting_force)
            load_inertia = calculate_load_inertia(screw_length, diameter_range, load, lead)
            
        else:  # 零件規格輸入
            st.markdown("**請輸入螺桿規格，系統將計算對應的物理參數並推薦：**")
            c1, c2 = st.columns(2)
            with c1:
                screw_diameter = st.number_input("螺桿公稱外徑 (mm)", value=40.0, min_value=10.0, max_value=100.0)
                screw_lead = st.number_input("螺桿導程 (mm)", value=12.0, min_value=1.0, max_value=50.0)
                screw_length = st.number_input("螺桿長度 (mm)", value=924.0, min_value=100.0)
            with c2:
                motor_max_speed = st.number_input("馬達最高轉速 (rpm)", value=4000.0, min_value=0.0)
                safety_factor = st.slider("安全係數", min_value=1.0, max_value=2.0, value=1.2, step=0.1)
                gravity_axis_YN = st.checkbox("重力軸", value=True)
            
            # 反向計算物理參數
            lead = screw_lead
            max_feed_rate = screw_lead * motor_max_speed  # 假設最大進給速率
            screw_max_speed = motor_max_speed
            diameter_range = [screw_diameter]  # 使用輸入的直徑
            
            # 估算負荷 (需要反向計算，這裡簡化)
            # 從動負荷估算負荷，這是近似值
            estimated_dynamic_load = 1000  # 預設值，需要更好的估算
            required_dynamic_load = estimated_dynamic_load
            
            # 估算扭矩和慣量
            load = 775  # 預設值
            cutting_force = 343  # 預設值
            required_motor_torque = calculate_motor_torque(lead, load, cutting_force)
            load_inertia = calculate_load_inertia(screw_length, diameter_range, load, lead)

# 左下：計算結果
with bottom_left:
    st.subheader("📊 計算分析結果")
    with st.container(border=True):
        st.markdown("**螺桿參數：**")
        st.write(f"導程: {lead:.1f} mm")
        st.write(f"最高轉速: {screw_max_speed:.1f} rpm")
        st.write(f"直徑範圍: {diameter_range}")
        st.write(f"動負荷需求: {required_dynamic_load} kgf")

        st.markdown("**馬達參數：**")
        st.write(f"扭矩需求: {required_motor_torque} N·m")
        st.write(f"附載慣量: {load_inertia} kgf·cm·s²")

# 右上：推薦
with top_right:
    st.subheader("🌟 系統推薦")
    
    # 重新計算按鈕
    if st.button("🔄 重新計算推薦", type="primary"):
        st.rerun()  # 重新運行整個應用
    
    screw_brand = st.selectbox("螺桿品牌", ["HIWIN", "PMI"])
    motor_brand = st.selectbox("馬達品牌", ["FANUC"])  # 目前只有 FANUC

    screw_recs = recommend_screws(screw_brand, lead, diameter_range, required_dynamic_load, safety_factor)
    motor_recs = recommend_motors(required_motor_torque, motor_max_speed, safety_factor)

    if screw_recs:
        st.markdown("**推薦螺桿：**")
        for rec in screw_recs[:3]:
            st.write(f"- {rec['型號']} (動負荷: {rec['動負荷 C (kfg)']} kgf)")
    else:
        st.write("無匹配螺桿")

    if motor_recs:
        st.markdown("**推薦馬達：**")
        for rec in motor_recs[:3]:
            st.write(f"- {rec['Model']} (扭矩: {rec['Value']} N·m)")
    else:
        st.write("無匹配馬達")

# 右中：自定義規格探索 (方案 B)
with top_right:
    st.markdown("---")
    st.subheader("🔧 方案 B：自定義規格探索")
    st.markdown("若對上方系統推薦的規格不滿意，可在此強制輸入您偏好的螺桿規格，系統將為您重新評估物理可行性。")
    
    # 使用 Toggle 開關讓介面更乾淨
    enable_custom = st.toggle("啟用自定義規格探索")
    
    if enable_custom:
        with st.container(border=True):
            c1, c2 = st.columns(2)
            with c1:
                # 預設帶入系統計算出的建議值
                custom_lead = st.number_input("自定義導程 (mm)", value=float(lead), min_value=1.0, step=1.0)
            with c2:
                # 預設帶入建議範圍的最小值
                default_dia = float(diameter_range[0]) if diameter_range else 40.0
                custom_diameter = st.number_input("自定義外徑 (mm)", value=default_dia, min_value=10.0, step=1.0)
            
            # --- 核心邏輯：反算物理參數 ---
            st.markdown("**🔍 該規格物理評估對比：**")
            
            # 重新計算新規格下的物理表現
            new_screw_max_speed = calculate_screw_max_speed(max_feed_rate, custom_lead)
            new_motor_torque = calculate_motor_torque(custom_lead, load, cutting_force)
            new_inertia = calculate_load_inertia(screw_length, [custom_diameter], load, custom_lead)
            
            # 使用 metric 顯示對比差異 (Delta)
            c3, c4, c5 = st.columns(3)
            # 轉速差異
            speed_diff = new_screw_max_speed - screw_max_speed
            c3.metric("所需最高轉速", f"{new_screw_max_speed:.0f} rpm", f"{speed_diff:.0f} rpm" if speed_diff != 0 else None, delta_color="inverse")
            
            # 扭矩差異
            torque_diff = new_motor_torque - required_motor_torque
            c4.metric("馬達扭矩需求", f"{new_motor_torque:.2f} N·m", f"{torque_diff:.2f} N·m" if torque_diff != 0 else None, delta_color="inverse")
            
            # 慣量差異
            inertia_diff = new_inertia - load_inertia
            c5.metric("附載慣量", f"{new_inertia:.2f}", f"{inertia_diff:.2f}" if inertia_diff != 0 else None, delta_color="inverse")
            
            # --- 重新推薦型號 ---
            st.markdown(f"**🌟 尋找 {screw_brand} 品牌中，外徑 {custom_diameter:.0f} / 導程 {custom_lead:.0f} 的型號：**")
            custom_screw_recs = recommend_screws(screw_brand, custom_lead, [custom_diameter], required_dynamic_load, safety_factor)
            
            if custom_screw_recs:
                for rec in custom_screw_recs[:3]:
                    st.write(f"- {rec['型號']} (動負荷: {rec['動負荷 C (kfg)']} kgf)")
            else:
                st.error("⚠️ 資料庫中無符合此自定義規格的型號，或該規格的動負荷無法滿足您設定的安全係數！")

# 右下：RAG 聊天
with bottom_right:
    st.subheader("💬 RAG 技術諮詢")
    
    # 初始化 session_state
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # 🔑 關鍵修改 1：建立一個「固定高度」且「具備獨立滾輪」的對話容器
    # height 的數值 (例如 400) 可以根據你的螢幕版面自由調整
    chat_container = st.container(height=400, border=True)

    # 🔑 關鍵修改 2：把歷史訊息畫在這個容器裡面
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg['role']):
                st.write(msg['content'])

    # st.chat_input 預設就會貼齊在容器的下方
    if prompt := st.chat_input("詢問技術問題..."):
        
        # 1. 儲存並顯示使用者的新問題
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        with chat_container:  # ⚠️ 確保新訊息也寫入獨立滾動區塊內
            with st.chat_message('user'):
                st.write(prompt)

        # 2. 準備 context 並呼叫模型
        context = f"推薦螺桿: {[rec['型號'] for rec in screw_recs[:3]]}, 計算參數: 導程 {lead}, 動負荷 {required_dynamic_load}"
        response = rag_query(prompt, context)
        
        # 3. 儲存並顯示 AI 的新回應
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        with chat_container:  # ⚠️ 確保新訊息也寫入獨立滾動區塊內
            with st.chat_message('assistant'):
                st.write(response)