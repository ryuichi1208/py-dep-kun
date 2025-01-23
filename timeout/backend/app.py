from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import time

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Sleep Example</title>
    </head>
    <body>
        <h1>WebSocket with Sleep</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8080/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            ws.onclose = function() {
                alert("Connection closed.");
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connected.")
    try:
        while True:
            try:
                # メッセージを受信
                data = await websocket.receive_text()
                print(f"Received: {data}")
                print("Processing...")
                time.sleep(3)
                # 応答を送信
                await websocket.send_text(f"Processed after sleep: {data}")
            except WebSocketDisconnect:
                print("WebSocket disconnected.")
                break
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("WebSocket connection closed.")
