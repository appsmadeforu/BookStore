from django.urls import path
from store import views
from django.conf.urls import url

urlpatterns = [
    path('', views.store),
    path('index/', views.index),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),
]
