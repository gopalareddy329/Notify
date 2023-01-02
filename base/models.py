import json
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync,sync_to_async
import uuid
from django.contrib.auth.hashers import make_password

class Broadcaste(models.Model):
    message=models.TextField()
    broadcaste=models.DateTimeField(auto_now_add=True)
    sent=models.BooleanField(default=False,editable=False)

    class Meta:
        ordering=['-broadcaste']

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    roomid=models.CharField(max_length=50,default=uuid.uuid4)
    participents=models.ManyToManyField(User,related_name="participents",blank=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name[:20]
        

class Message(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField(blank=False,null=False)
    Room=models.ForeignKey(Room,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    def __str__(self):
        return self.body[0:50]



@receiver(post_save,sender=Broadcaste)
def notification_handler(sender,instance,created,**kwargs):
    channel_layer=get_channel_layer()
    
    data={'notification':instance.message,'time':str(instance.broadcaste)}
    async_to_sync(channel_layer.group_send)(
        'chat_universal',
        {
        "type":"broadcaste",
        "message":json.dumps(data)
        }
    )
    Broadcaste.objects.filter(id=instance.id).update(sent=True)
    


    
