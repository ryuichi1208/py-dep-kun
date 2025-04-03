# WebSocketアプリケーション負荷テスト

このリポジトリには、WebSocketを使用したアプリケーションとその負荷テストスクリプトが含まれています。

## アプリケーションの構成

- バックエンド: FastAPI（WebSocketサポート）
- プロキシ: Nginx
- 構成管理: Docker Compose

## 負荷テストスクリプト

k6を使用した2つの負荷テストスクリプトを提供しています：

1. `k6-test.js` - 基本的なHTTPとWebSocketの負荷テスト
2. `k6-timeout-test.js` - WebSocketのタイムアウト動作を検証するテスト

## 実行方法

### アプリケーションの起動

```bash
docker-compose up -d
```

### 負荷テストの実行

基本的な負荷テスト:
```bash
k6 run k6-test.js
```

タイムアウトテスト:
```bash
k6 run k6-timeout-test.js
```

## k6のインストール

k6をインストールしていない場合は、以下の方法でインストールできます：

### macOS
```bash
brew install k6
```

### Linux
```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update
sudo apt-get install k6
```

### Docker
```bash
docker pull loadimpact/k6
docker run -i loadimpact/k6 run - <k6-test.js
```
