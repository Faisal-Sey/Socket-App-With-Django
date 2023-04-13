# chat/consumers.py

import json
from random import randint
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
      # Generate a unique channel name based on the user, e.g., using the user ID
      channel_name = "user_1"

      # Add the user's channel to a group
      await self.channel_layer.group_add(channel_name, self.channel_name)

      # Accept the WebSocket connection
      await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def chat_message(self, event):
      # Send the chat message as an event with event name to the WebSocket
      await self.send(text_data=json.dumps(event['message']))
