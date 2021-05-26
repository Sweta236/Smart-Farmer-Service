from django.contrib import admin
from django.urls import path,include
from . import views

app_name='marketprice'
urlpatterns = [
    path("add_mprice/", views.add_marketPrice, name="add_marketPrice"),

    path("search_mprice/", views.Search_mprice, name="Search_mprice"),
]