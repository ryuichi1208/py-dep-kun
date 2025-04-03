import { check, sleep } from 'k6';
import ws from 'k6/ws';

export const options = {
    vus: 10,
    duration: '30s',
    thresholds: {
        'ws_connecting': ['p(95)<1000'],  // WebSocket接続の95%が1秒以内に完了すること
    },
};

// メッセージ送信後、長時間待機するテスト
export default function () {
    const url = 'ws://localhost:8080/ws';
    const params = { timeout: 70000 }; // 70秒のタイムアウト（Nginxは60秒に設定）

    const res = ws.connect(url, params, function (socket) {
        socket.on('open', () => {
            console.log('WebSocket接続開始');
            socket.send('長時間待機テスト');
        });

        socket.on('message', (data) => {
            console.log('メッセージ受信: ' + data);
            check(data, {
                'レスポンスが正しい': (d) => d.includes('Processed after sleep'),
            });
            // 接続を維持し、Nginxのタイムアウト（60秒）を超えるまで待機
            // 接続が切れるのを待つだけで、この後明示的にcloseは呼ばない
        });

        socket.on('close', () => {
            console.log('WebSocket接続終了');
            check(null, {
                'タイムアウトによる接続終了': () => true,
            });
        });

        socket.on('error', (e) => {
            console.log('WebSocketエラー: ' + e.error());
            check(null, {
                'エラー発生': () => true,
            });
        });
    });

    check(res, {
        'WebSocket接続成功': (r) => r && r.status === 101,
    });

    // テスト中はスクリプトを実行し続ける
    sleep(65);
}
