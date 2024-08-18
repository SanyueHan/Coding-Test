from typing import Dict

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self._active_connections: Dict[int, WebSocket] = {}
        self._id_to_name = {}

    async def connect(self, client_id, websocket: WebSocket):
        await websocket.accept()
        self._active_connections[client_id] = websocket

    def disconnect(self, client_id):
        if client_id in self._active_connections:
            self._active_connections.pop(client_id)
        if client_id in self._id_to_name:
            self._id_to_name.pop(client_id)

    async def broadcast(self, message: str):
        for connection in self._active_connections.values():
            await connection.send_text(message)

    def get_client_name(self, client_id):
        return self._id_to_name.get(client_id)

    def set_client_name(self, client_id, name):
        self._id_to_name[client_id] = name
