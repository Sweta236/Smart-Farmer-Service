from django.contrib import admin
from django.urls import path,include
from . import views

app_name='machine'
urlpatterns = [
    path("buy_machine/", views.buy_machine, name="buy_machine"),
    path("buy_machine/cart_machine/", views.cart_machine, name="cart_machine"),
    path("add_machine/", views.add_machine, name="add_machine"),

    path('buy_machine/cart_machine/success_mac', views.success_mac, name="success_mac"),
]