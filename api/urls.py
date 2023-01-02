from django.urls import path
from . import views
urlpatterns=[
    path('api-auth/',views.home),
    path('api-auth/details/<str:no>',views.Roomdetails,name="Roomdetails"),
    path('api-auth/create',views.CreateRoom,name="Createroom"),
    path('api-auth/update/<str:no>',views.UpdateRoom,name="updateroom")
]