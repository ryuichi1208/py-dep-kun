import http from 'k6/http';
import { check, sleep } from 'k6';
import ws from 'k6/ws';

export const options = {
    stages: [
        { duration: '30s', target: 20 }, // 30秒かけて20ユーザーまで増加
        { duration: '1m', target: 20 },  // 1分間20ユーザーを維持
        { duration: '30s', target: 0 },  // 30秒かけて0ユーザーまで減少
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95%のリクエストが500ms以下であること
        'ws_connecting': ['p(95)<1000'],  // WebSocket接続の95%が1秒以内に完了すること
    },
};

// HTTPエンドポイントのテスト
export function httpTest() {
    const res = http.get('http://localhost:8080/');
    check(res, {
        'HTTPステータスが200': (r) => r.status === 200,
        'レスポンスにHTMLが含まれている': (r) => r.body.includes('WebSocket Sleep Example'),
    });
    sleep(1);
}

// WebSocketのテスト
export function wsTest() {
    const url = 'ws://localhost:8080/ws';
    const params = { timeout: 10000 };

    const res = ws.connect(url, params, function (socket) {
        socket.on('open', () => {
            console.log('WebSocket接続開始');
            socket.send('テストメッセージ');
        });

        socket.on('message', (data) => {
            console.log('メッセージ受信: ' + data);
            check(data, {
                'レスポンスに "Processed after sleep" が含まれている': (d) => d.includes('Processed after sleep'),
            });
            socket.close();
        });

        socket.on('close', () => console.log('WebSocket接続終了'));
        socket.on('error', (e) => console.log('WebSocketエラー: ' + e.error()));

        socket.setTimeout(function () {
            console.log('3秒後に接続を閉じる');
            socket.close();
        }, 3000);
    });

    check(res, {
        'WebSocket接続成功': (r) => r && r.status === 101,
    });
}

// 両方のテストを実行
export default function () {
    httpTest();
    wsTest();
    sleep(1);
}
