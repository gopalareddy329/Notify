from django.urls import path
from . import client

websocket_urlpatterns=[
    path("ws/<str:room_id>/",client.ChatConsumer.as_asgi()),
    path("ws/room/<str:room_id>/",client.Groupchat.as_asgi()),
]