from django.urls import path
from store import views

urlpatterns = [
    path('', views.store),
    path('index/', views.index),
]