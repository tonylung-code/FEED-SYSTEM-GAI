import streamlit as st

# --- [1. 頁面設定] ---
st.set_page_config(page_title="HIWIN 智慧選型系統", layout="wide")

# --- [2. 自定義 CSS] ---
# 這裡加入 CSS 讓左側面板在捲動時能儘量保持在視線內 (Sticky)
st.markdown("""
    <style>
    /* 強烈建議的推薦框樣式 */
    .recommendation-box {
        background-color: #1E3A8A;
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    .recommendation-box h4 { color: white !important; margin: 0; }
    
    /* 放大字體的樣式 */
    .big-font {
        font-size: 26px !important;
        font-weight: bold;
        line-height: 1.6;
    }
    
    /* 讓左側欄位在捲動時稍微固定 (僅在桌面版有效) */
    [data-testid="stVerticalBlock"] > div:first-child {
        position: -webkit-sticky;
        position: sticky;
        top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

guide = 12


# --- [主頁面佈局] ---
# 使用 gap="medium" 讓視覺更緊湊
left_col, right_col = st.columns([1, 1.2], gap="medium")

# --- [左側：輸入與計算結果] ---
with left_col:
    st.subheader("🛠️ 使用者設計條件")
    with st.container(border=True):
        c_in1, c_in2 = st.columns(2)
        with c_in1:
            max_feed = st.number_input("最大進給速率 (mm/min)", value=48000)
            motor_speed = st.number_input("馬達最高轉速 (rpm)", value=4000)
            axis_type = st.selectbox("選取軸向", ["x", "y", "z"])
        with c_in2:
            load_val = st.number_input("負載 (kg)", value=775)
            screw_len = st.number_input("螺桿長度 (mm)", value=924)
            gravity_yn = st.checkbox("判斷為重力軸", value=True)

    st.divider()

    st.subheader("📊 計算分析結果")
    with st.container(border=True):
        # 使用 HTML 標籤直接放大字體，不使用 Markdown
        st.markdown('<p style="font-size: 18px; margin-bottom: 5px;">【螺桿參數計算】</p>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="big-font">
                挫曲桿徑: {15.0} mm <br>
                臨界轉速桿徑: 8.0 mm <br>
                直徑範圍: 15.0 ~ 38.0 mm <br>
                建議導程: {guide} <br>
                建議動負荷: 7453.0 kgf
            </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown('<p style="font-size: 18px; margin-bottom: 5px;">【馬達計算結果】</p>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="big-font">
                總扭矩: 22.03 N-mm <br>
                負載慣量: 0.0473 kgf-cm-s2
            </div>
        """, unsafe_allow_html=True)

# --- [右側：推薦型號與對話] ---
with right_col:
    # --- 右上：推薦型號 (置頂且固定) ---
    st.subheader("🌟 系統最終推薦")
    st.markdown('<div class="recommendation-box"><h4>推薦型號：FDC 40-12K5</h4></div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        adj_c1, adj_c2, adj_c3 = st.columns([1.2, 1, 0.8])
        with adj_c1:
            f_series = st.selectbox("系列更改", ["FDC", "FSW", "FSV", "FSI"], index=0)
            f_dia = st.selectbox("直徑更改 (mm)", [15, 20, 25, 32, 40], index=4)
        with adj_c2:
            f_lead = st.selectbox("導程更改 (mm)", [5, 10, 12, 16, 20], index=2)
            st.write(f"**確認規格:** \n{f_series} {f_dia}-{f_lead}")
        with adj_c3:
            # 產品圖縮小
            st.image("https://www.hiwin.tw/images/products/bs/fdc.jpg", use_container_width=True)

    st.divider()

    # --- 右下：大聊天視窗 ---
    st.subheader("💬 技術諮詢視窗 (RAG)")
    
    # 這裡的關鍵是 height，設定足夠的高度讓它內部滾動，而不會撐開整個頁面
    chat_container = st.container(height=600)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "針對推薦規格，有任何技術疑問嗎？"}]

    for msg in st.session_state.messages:
        chat_container.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("請輸入問題..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        chat_container.chat_message("user").write(prompt)
        with chat_container.chat_message("assistant"):
            st.write("（RAG 檢索中...）")