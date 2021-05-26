from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="home"),
    path('home', views.index, name="home"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),

]
