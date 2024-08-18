from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from html import HTML_MULTI_CLIENT

from connection_manager import ConnectionManager


app = FastAPI()

manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(HTML_MULTI_CLIENT)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(client_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            if name := manager.get_client_name(client_id):
                await manager.broadcast(f"{name}: {data}")
            else:
                if data:
                    manager.set_client_name(client_id, data)
                    await websocket.send_text(f"Your name is {data}")
                else:
                    await websocket.send_text("Invalid name")
    except WebSocketDisconnect:
        name = manager.get_client_name(client_id)
        manager.disconnect(client_id)
        await manager.broadcast(f"{name if name else client_id} left the chat")
