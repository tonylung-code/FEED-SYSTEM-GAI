import streamlit as st
import pandas as pd
import Formula_set_lookup as fsl  # 核心計算模組

# 嘗試載入 RAG 套件
try:
    import chromadb
    import ollama
    from chromadb.config import Settings
    RAG_AVAILABLE = True
except ImportError:
    RAG_AVAILABLE = False

# --- [1. 頁面設定] ---

st.set_page_config(page_title="進給系統智慧計算選型系統", layout="wide")
st.markdown("""
    <style>

    /* 1. 讓 st.subheader (h3) 統一變成 24px、深藍色、加粗 */
    h3, div[data-testid="stMarkdownContainer"] h3, [data-testid="stHeader"] h3 {
        font-size: 24px !important;
        color: #1E3A8A !important;
        font-weight: bold !important;
        margin-top: 10px !important;
        margin-bottom: 5px !important;
    }

    /* 2. 輸入元件標題與 Checkbox (18px) */
    div[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"] span,
    div[data-testid="stCheckbox"] p,
    div[data-testid="stCheckbox"] label span {
        font-size: 18px !important;
        font-weight: bold !important;
        color: #1E3A8A !important;
    }
    
    /* 3. 放大輸入框裡面的數字與下拉選單文字 (20px) */
    input[type="number"], 
    input[type="text"],
    div[data-baseweb="select"] div,
    div[data-baseweb="select"] span {
        font-size: 20px !important;
    }
            
    /* 4. 針對 st.write() 和 一般 st.markdown() 輸出的文字 (20px) */
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] span,
    div[data-testid="stMarkdownContainer"] li,
    div[data-testid="stText"] {
        font-size: 20px !important;
        line-height: 1.6 !important;
    }

    /* 5. 讓推薦型號的 DataFrame 表格文字也變成 20px */
    div[data-testid="stDataFrame"] div,
    table[data-testid="stTable"] th,
    table[data-testid="stTable"] td {
        font-size: 20px !important;
    }

    /* 6. 讓分頁標籤 (Tabs) 與 按鈕 (Buttons) 裡的字也變成 20px */
    button p, 
    button span,
    div[data-baseweb="tab"] p, 
    div[data-baseweb="tab"] div,
    div[data-baseweb="tab"] span {
        font-size: 20px !important;
    }

    /* 7. 保留給大標題使用的樣式 */
    div.big-font { 
        font-size: 28px !important; 
        font-weight: bold !important; 
        color: #1E3A8A !important; 
    }
    </style>
""", unsafe_allow_html=True)

# --- [2. 主頁面四象限佈局] ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    top_left = st.container()
    bottom_left = st.container()
with col2:
    top_right = st.container()
    bottom_right = st.container()

#左上：輸入參數區塊
# ==========================================
with top_left:
    st.markdown("<div style='font-size: 30px; font-weight: bold; margin-top: 5px; color: #1E3A8A; margin-bottom: 8px;'>🛠️ 使用者設計條件結果</div>", unsafe_allow_html=True)
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            maximum_feed_rate = st.number_input("最大進給速率 (mm/min)", value=48000, step=1000)
            motor_max_speed = st.number_input("馬達最高轉速 (rpm)", value=3000, step=100)
            reduction_ratio = st.number_input("減速比", value=1.0, step=0.1)
            load = st.number_input("負載 (kgf)", value=775, step=10)
            cutting_force = st.number_input("切削力 (kgf)", value=343, step=10)
        with c2:
            length = st.number_input("行程 (mm)", value=924, step=10)
            preload_rate = st.number_input("預壓率", value=0.05, step=0.01, format="%.2f")
            gravity_axis_YN = st.checkbox("是否為重力軸?", value=True)
            support_type = st.selectbox("支撐類型", ["fixed_supported", "supported_supported", "fixed_fixed", "fixed_free"])
            combination = st.selectbox("軸承組合類型", ["DF", "DFD", "DFF"])

ui_params = {
            "maximum_feed_rate": maximum_feed_rate,
            "motor_max_speed": motor_max_speed,
            "reduction_ratio": reduction_ratio,
            "load": load,
            "cutting_force": cutting_force,
            "length": length,
            "preload_rate": preload_rate,
            "gravity_axis_YN": gravity_axis_YN,
            "support_type": support_type,
            "combination": combination
        }
#核心運算觸發
# ==========================================
try:
    calc_results = fsl.run_ballscrew_calculation(ui_params)
    calc_success = True
except Exception as e:
    st.error(f"計算核心發生錯誤: {e}")
    calc_success = False

#左下：計算分析結果
# ==========================================
if calc_success:
    with bottom_left:
        st.markdown("<div style='font-size: 30px; font-weight: bold; margin-top: 5px; color: #1E3A8A; margin-bottom: 8px;'>🔩物理參數分析結果</div>", unsafe_allow_html=True)
        with st.container(border=True):
            
            st.markdown("<div style='font-size: 22px; font-weight: bold; margin-top: 5px; margin-bottom: 8px;'>螺桿基礎參數</div>", unsafe_allow_html=True)
            st.write(f"- 系統建議導程: **{calc_results.get('guide')}** mm")
            st.write(f"- 計算動負荷: **{calc_results.get('dynamic_load')}** kgf")
            
            st.markdown("<div style='font-size: 22px; font-weight: bold; margin-top: 5px; margin-bottom: 8px;'>螺桿安全驗證</div>", unsafe_allow_html=True)
            # 這裡對應您字典中可能包裝的 key，若為扁平結構請依您的實際 key 調整
            st.write(f"- 容許臨界轉速: **{calc_results.get('allowable_speed', 0):.2f}** rpm")
            st.write(f"- 容許最大壓縮力(挫曲): **{calc_results.get('allowable_buckling', 0):.2f}** kgf")
            st.write(f"- 容許最大拉伸力: **{calc_results.get('allowable_tensile', 0):.2f}** kgf")

            st.markdown("<div style='font-size: 22px; font-weight: bold; margin-top: 5px; margin-bottom: 8px;'>馬達匹配參數</div>", unsafe_allow_html=True)
            st.write(f"- 系統總扭矩 (Trf): **{calc_results.get('torque')}** N.m")
            st.write(f"- 負載慣量 (JL): **{calc_results.get('inertia')}** kgf．cm．s2")

#右上：推薦系統 (DataFrames)
# ==========================================
if calc_success:
    with top_right:
        st.markdown("<div style='font-size: 30px; font-weight: bold; margin-top: 5px; color: #1E3A8A; margin-bottom: 8px;'>🌟 系統推薦型號</div>", unsafe_allow_html=True)
        
        
        recs = calc_results.get("recommendations", {})
        
        # 使用 Streamlit 的 Tabs 分頁顯示不同品牌
        tab1, tab2 = st.tabs(["HIWIN 推薦規格", "PMI 推薦規格"])
        
        with tab1:
            hiwin_data = recs.get("HIWIN")
            if isinstance(hiwin_data, pd.DataFrame):
                st.dataframe(hiwin_data, use_container_width=True, hide_index=True)
            else:
                st.warning(hiwin_data) # 顯示字串警告訊息
                
        with tab2:
            pmi_data = recs.get("PMI")
            if isinstance(pmi_data, pd.DataFrame):
                st.dataframe(pmi_data, use_container_width=True, hide_index=True)
            else:
                st.warning(pmi_data)

#右下：RAG 聊天室
# ==========================================
with bottom_right:
    st.markdown("<div style='font-size: 30px; font-weight: bold; margin-top: 5px; color: #1E3A8A; margin-bottom: 8px;'>AI 技術助理</div>", unsafe_allow_html=True)

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    chat_container = st.container(height=350, border=True)

    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg['role']):
                st.write(msg['content'])

    if prompt := st.chat_input("詢問規格差異或技術問題..."):
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        with chat_container:
            with st.chat_message('user'):
                st.write(prompt)

        # 這裡組合動態 Context 餵給 AI
        if calc_success:
            context = f"目前計算參數：建議導程 {calc_results.get('guide')} mm, 動負荷 {calc_results.get('dynamic_load')} kgf, 馬達扭矩 {calc_results.get('torque')} N.m"
        else:
            context = "尚未成功計算參數。"

        # 簡單的 Echo 測試或銜接您的 RAG API
        if RAG_AVAILABLE:
            # 此處可替換為您原本的 rag_query 函式
            response = "（AI 助理分析中...請在此處接回您原本的 ollama 呼叫代碼）" 
        else:
            response = f"系統目前未連接 Ollama，但已收到您的問題與當前環境參數：\n{context}"
        
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        st.rerun()

#def test_integration():
    print("啟動測試：嘗試呼叫 Formula_set_lookup 模組...")
    print("-" * 50)

    # 1. 模擬未來從 Streamlit UI 獲取的表單輸入參數
    mock_ui_inputs = {
        "maximum_feed_rate": 48000,
        "motor_max_speed": 3000,
        "reduction_ratio": 1,
        "load": 775,
        "cutting_force": 343,
        "length": 924,
        "preload_rate": 0.05,
        "gravity_axis_YN": True,
        "support_type": "fixed_supported",
        "combination": "DF"
    }

    try:
        # 2. 呼叫目標副程式
        print(">> 正在執行運算...")
        result_data = fsl.run_ballscrew_calculation(mock_ui_inputs)
        
        # 3. 驗證回傳結果
        print("\n✅ 測試成功！成功獲取回傳資料")
        print("-" * 50)
        print(f"🔹 系統建議導程: {result_data.get('guide')} mm")
        print(f"🔹 計算動負荷: {result_data.get('dynamic_load')} kgf")
        print(f"🔹 容許臨界轉速_rpm: {result_data.get('allowable_speed')}")
        print(f"🔹 容許最大壓縮力(挫曲)_kgf: {result_data.get('allowable_buckling')}")
        print(f"🔹 容許最大拉伸力_kgf: {result_data.get('allowable_tensile')}")
        print(f"🔹 馬達扭矩 (Trf): {result_data.get('torque')} N.m")
        print(f"🔹 馬達慣量 (JL): {result_data.get('inertia')} kgf．cm．s2")
        print("\n螺桿推薦型號:")
        for brand, result in result_data["recommendations"].items():
            print(f"\n[{brand}]")
            if isinstance(result, pd.DataFrame):
                print(result.to_string(index=False))
            else:
                print(result)
            
    except Exception as e:
        print(f"\n❌ 呼叫副程式時發生錯誤：\n{e}")

# if __name__ == "__main__":
#     test_integration()