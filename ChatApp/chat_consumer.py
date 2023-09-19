import json
from channels.generic.websocket import AsyncWebsocketConsumer


class Chat(AsyncWebsocketConsumer):
    # 连接
    async def connect(self):
        await self.accept()

    # 断开连接
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps(
            {'message': message}
        ))
