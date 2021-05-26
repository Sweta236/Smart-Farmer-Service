from django.contrib import admin
from django.urls import path,include
from . import views

app_name='crop'
urlpatterns = [
    path("buy_crop/", views.buy_crop, name="buy_crop"),
    path("buy_crop/cart_crop/", views.cart_crop, name="cart_crop"),
    path("add_crop/", views.add_crop, name="add_crop"),
path('buy_crop/cart_crop/success_c', views.success_c, name="success_c"),

]