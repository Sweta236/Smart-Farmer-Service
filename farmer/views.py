from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.apps import apps

# Create your views here.
def index(request):
    return render(request,'farmerHome.html')

def machine(request):
    return render(request,'machine.html')

def cro_guid(request):
    return render(request,'crop_guidlines.html')

def gov_schema(request):
    return render(request,'govschema.html')

def loan(request):
    return  render(request,'loan.html')