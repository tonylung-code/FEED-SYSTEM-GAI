# 1. 選擇基底鏡像
FROM python:3.12-slim

# 2. 設定容器內的工作目錄
WORKDIR /app

# 3. 複製套件清單並安裝
# 這裡先複製 requirements.txt 是為了利用 Docker 快取機制，加速以後的 Build 過程
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 複製專案剩餘的所有檔案到容器中
COPY . .

# 5. 設定程式啟動指令
# 假設你的主程式是 app.py
CMD ["streamlit", "run", "code/04_applications/scripts/app_simple_v3.py"]