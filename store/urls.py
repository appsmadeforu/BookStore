from django.urls import path
from store import views
from django.conf.urls import url

urlpatterns = [
    path('', views.store),
    path('index/', views.index),
    url('book/(\d+)', views.book_details, name='book_details'),
]
