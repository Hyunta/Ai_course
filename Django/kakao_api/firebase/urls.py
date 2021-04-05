from django.urls import path
from . import views

urlpatterns = [
    path('firebase-messaging-sw.js', views.fms),
    path('push', views.push),
    path('send', views.send),
]