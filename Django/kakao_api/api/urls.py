from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('mainpage', views.mainpage),
    path('friends', views.friends),
]