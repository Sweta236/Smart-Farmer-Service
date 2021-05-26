from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'farmer'
urlpatterns = [
    path('', views.index, name="home"),
    path('m', views.machine, name="machine"),
    path('crop_guid', views.cro_guid, name="cro_guid"),
    path('govschema', views.gov_schema, name="govschema"),
    path('loan', views.loan, name="loan"),

]