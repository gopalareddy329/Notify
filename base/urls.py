from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('join/',views.join,name="join"),
    path('signup/',views.signup,name="signup"),
    path('createroom/',views.createroom,name="createroom"),
    path('deleteroom/',views.deleteroom,name="deleteroom"),
]