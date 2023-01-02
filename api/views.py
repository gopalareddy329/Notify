from django.shortcuts import render
from rest_framework.decorators import api_view
from base.models import Room,Message
from .serializers import RoomSerializer
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
@api_view(['GET'])
def home(request):
    if request.method=="GET":
        rooms=Room.objects.all()
        serializer=RoomSerializer(rooms,many=True)

        return Response(serializer.data)

@api_view(['GET'])
def Roomdetails(request,no):
    if request.method=="GET":
        rooms=Room.objects.get(roomid=no)
        serializer=RoomSerializer(rooms,many=False)

        return Response(serializer.data)

@api_view(['POST'])
def CreateRoom(request):
        serializer=RoomSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def UpdateRoom(request,no):
        rooms=Room.objects.get(roomid=no)
        serializer=RoomSerializer(instance=rooms,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

