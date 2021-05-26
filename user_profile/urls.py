from django.contrib import admin
from django.urls import path,include
from . import views

app_name='user_profile'
urlpatterns = [
    path("agri_profile/", views.agri_profile, name="agri_profile"),
    path("agri_profile/edit/<int:id>", views.update_agri, name="update_agri"),
    path("agri_profile/delete/<int:id>", views.delete_agri, name="delete_agri"),
    path("myard_profile/", views.MYO_profile, name="MYO_profile"),
    path("myard_profile/delete/<int:id>", views.delete_price, name="delete_price"),
    path("myard_profile/edit/<int:id>", views.update_price, name="update_price"),

    path('farmer_profile',views.farmer_profile,name="farmer_profile"),
    path('farmer_profile/f_profile',views.f_profile,name="f_profile"),

    path('farmer_profile/f_crop',views.f_crop,name="f_crop"),
    path('farmer_profile/f_crop/edit/<int:id>',views.update_crop,name="update_crop"),
    path('farmer_profile/f_crop/delete/<int:id>',views.delete_crop,name="delete_crop"),

    path('farmer_profile/f_agri',views.f_agri,name="f_agri"),


    path('farmer_profile/f_machine',views.f_machine,name="f_machine"),
    path('farmer_profile/f_machine/edit/<int:id>',views.update_machine,name="update_machine"),
    path('farmer_profile/f_machine/delete/<int:id>',views.delete_machine,name="delete_machine"),



]