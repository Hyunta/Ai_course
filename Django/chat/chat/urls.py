from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('settoken', views.settoken),
    path('friends', views.friends),
    path('chat', views.chat),
    path('firebase-messaging-sw.js', views.fms),
]