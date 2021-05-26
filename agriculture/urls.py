from django.contrib import admin
from django.urls import path,include
from . import views

app_name='agriculture'
urlpatterns = [
    path("buy_agri/", views.buy_agri, name="buy_agri"),
    path("buy_agri/cart_agri/", views.cart_agri, name="cart_agri"),
    path("add_agri/", views.add_agri, name="add_agri"),
path('buy_agri/cart_agri/success_agri', views.success_agri, name="success_agri"),
]