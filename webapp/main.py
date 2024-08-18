from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from html import HTML


app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse(HTML)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
