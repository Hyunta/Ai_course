from django.urls import path
from . import views

urlpatterns = [
    path('webtoon', views.webtoon),
    path('gourmet', views.gourmet),
]