import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async,async_to_sync
from base.models import Room,Message
from django.contrib.auth.models import User
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_id=self.scope['url_route']['kwargs']['room_id']
        self.room_group_name="chat_%s" % self.room_id
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self,event):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    def broadcaste(self,data):
        message=data['message']
        self.send(json.dumps({'message':message}))

class Groupchat(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomid=self.scope['url_route']['kwargs']['room_id']
        self.room_group_name="chat_%s"%self.roomid
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self,event):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
        
    async def receive(self, text_data):
        text_data=json.loads(text_data)

        message=str(text_data["message"])
        username=text_data["username"]
        roomid=text_data["room"]
        await self.channel_layer.group_send(
            
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'room':roomid
            }
        )
        

    async def chat_message(self,event):
        message=str(event["message"])
        username=event["username"]
        roomid=event["room"]
        
        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'room':roomid
        }))


        



    

