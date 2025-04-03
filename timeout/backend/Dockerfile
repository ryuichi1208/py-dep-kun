# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN pip install gunicorn fastapi uvicorn uvicorn[standard] httpx

# アプリケーションコードをコピー
COPY app.py .

# uvicornサーバーを起動
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["gunicorn", "-c", "/app/gunicorn_conf.py", "app:app"]
