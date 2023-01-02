import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Broadcaste,Room,Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from channels.layers import get_channel_layer
from asgiref.sync import sync_to_async,async_to_sync
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        data=Broadcaste.objects.all()
        search=request.GET.get('q')  if request.GET.get('q') != None else ""
        #Rooms=Room.objects.filter(Q(name__icontains=search)|Q(roomid=search))

        Rooms=Room.objects.filter(Q(host=request.user) | Q(participents=request.user))
        
        Rooms=Rooms.filter(Q(roomid=search)|Q(name__icontains=search))
        Rooms=Rooms.order_by('host').distinct()
        context={'rooms':Rooms,'Data':data}
        try:
            if request.method=="POST":
                roomid=request.POST.get("roomid")
                room=Room.objects.get(roomid=roomid)
                participents=room.participents.all()
                members=room.participents.contains(request.user)
                members=True if request.user ==room.host else members
                try:
                    rmessage=request.POST.get("user-sending")
                    user=User.objects.get(username=request.user)
                    Message.objects.create(host=user,body=rmessage,Room=room)
                except:pass
                if members:
                    messages=room.message_set.all()
                    context['room']=room
                    context['messages']=messages
                    context['participents']=participents
                    return render(request,'home.html',context)
            return render(request,'home.html',context)
        except:
            return redirect('home') 
    return render(request,'home.html')

def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            return render(request,'home.html',{"error":"Invalid username"})
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home') 
        else:
            return render(request,'home.html',{"error":"Invalid Password"})
    return redirect('home') 
def logout_user(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=username+"@notify.com"
        try:
            user=User.objects.create_user(username=username,password=password,email=email)
            login(request,user)

            return redirect('home')
        except:
            return render(request,'home.html',{"error":"Username Already Exisit"})
    return redirect('home')

@login_required(login_url="home")
def join(request):
    if request.method=="POST":
        roomid=request.POST.get("joinid")
        try:
            room=Room.objects.get(roomid=roomid)
            if request.user !=room.host:

                user=room.participents.contains(request.user)
                if user==False:
                    Message.objects.create(Room=room,host=request.user,body="Joined")
                    channel_layer=get_channel_layer()

                    async_to_sync(channel_layer.group_send)(
                            'chat_%s'%roomid,
                            {
                            'type':'chat_message',
                            'message':"Joined",
                            'username':str(request.user.username),
                            'room':str(roomid)
                            }
                        )
                    room.participents.add(request.user)

                    redirect('home')
                else:
                    return render(request,'home.html',{"error":"Already Exisit"})
        except:
            return render(request,'home.html',{"error":"Invalid Roomid"})
    return redirect('home')
@login_required(login_url="home")
def createroom(request):
    if request.method=="POST":
        try:
            roomname=request.POST.get("createid")
            Room.objects.create(host=request.user,name=roomname)
        except:
            return render(request,'home.html',{"error":"Error to create room"})

    return redirect('home')


@login_required(login_url="home")
def deleteroom(request):
    try:
        participent=Room.objects.filter(Q(participents=request.user)|Q(host=request.user))
        if request.method=='POST':
            roomid=request.POST.get("deleteroomid")
            room=Room.objects.get(roomid=roomid)
            if request.user==room.host:
                room.delete()
            else:
                
                room.participents.remove(request.user)
            return redirect("home")
    except:
        return redirect("home")
    return render(request,'home.html',{"userrooms":participent})