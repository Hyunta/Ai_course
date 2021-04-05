from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('read', views.read),
    path('list', views.list),
    path('delete', views.delete),
    path('modify', views.modify),

]