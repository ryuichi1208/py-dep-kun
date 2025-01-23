# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN pip install fastapi uvicorn uvicorn[standard]

# アプリケーションコードをコピー
COPY app.py .

# uvicornサーバーを起動
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
