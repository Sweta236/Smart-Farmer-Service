from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from crop.models import *
from agriculture.models import *
from machine.models import *


def index(request):
    return render(request, 'AdminLogin.html')


def loginAdmin(request):
    if request.method == "POST":
        name = request.POST['name']
        pwd = request.POST['pass']
        if (name == "Admin" and pwd == "Admin@678"):
            cr_p = Order_crop.objects.all().count()
            ag_p = Order_agri.objects.all().count()
            mac_p = Order_machine.objects.all().count()

            data = {'cr_p': cr_p, 'ag_p': ag_p, 'mac_p': mac_p}
            return render(request, 'dashboard.html', data)
        else:
            return render(request, 'AdminLogin.html')
    else:
        return render(request, 'AdminLogin.html')



def added_c(request):
    crop_p = crop.objects.all()
    data = {'crop_p': crop_p}
    return render(request, 'product_added/crop.html', data)


def added_a(request):
    agri_p = agri.objects.all()
    data = {'agri_p': agri_p}
    return render(request, 'product_added/agri.html', data)


def added_mac(request):
    mac = machine.objects.all()
    data = {'mac': mac}
    return render(request, 'product_added/machine.html', data)


def order_crop_p(request):
    order_c = Order_crop.objects.all()

    data = {'order_c': order_c}
    return render(request, 'order_product/order_crop.html', data)


def order_agri_p(request):
    order_a = Order_agri.objects.all()
    data = {'order_a': order_a}
    return render(request, 'order_product/order_agri.html', data)


def order_mac(request):
    o_mac = Order_machine.objects.all()
    data = {'o_mac': o_mac}
    return render(request, 'order_product/order_machine.html', data)
