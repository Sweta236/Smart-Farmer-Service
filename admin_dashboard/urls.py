from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'admin_dashboard'
urlpatterns = [
    path('home', views.index, name="home"),
    path('loginAdmin', views.loginAdmin, name="loginAdmin"),

    path('crop_p', views.added_c, name="added_c"),
    path('agri_p', views.added_a, name="added_a"),
    path('machine', views.added_mac, name="added_mac"),

    path('order_crop_p', views.order_crop_p, name="order_crop_p"),
    path('order_agri_p', views.order_agri_p, name="order_agri_p"),
    path('order_mac', views.order_mac, name="order_mac"),

]