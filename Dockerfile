# 使用 Python 3.9 slim 作為基礎映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製應用程式檔案到容器
COPY . /app

# 安裝 Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 啟動 Streamlit 應用
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
