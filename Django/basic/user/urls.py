from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    path('login', views.login),
    path('do_login', views.do_login)
]