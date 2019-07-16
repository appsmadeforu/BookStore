from django.urls import path
from store import views

urlpatterns = [
    path('', views.index),
    path('books/', views.bookss)

]