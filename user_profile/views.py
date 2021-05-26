from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.apps import apps
from agriculture. models import *
from crop.models import *
from  machine.models import *
from marketprice. models import *
from django.contrib.auth.models import auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
import ast
from accounts.models import User
import razorpay

# Create your views here.
def agri_profile(request):
    user = request.user
    u = User.objects.all()
    agri_p = agri.objects.all()
    o_agri = Order_agri.objects.all()
    # if request.method=='POST':
    #    img=request.POST.get('image')
    #    user = User.objects.get(username=request.user)
    #    user.profile_pic = img
    #    user.save()
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        # mobile=request.POST.get('mbl')
        add = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip_code')

        user = User.objects.get(username=request.user)

        user.uname = uname
        user.email = email
        # user.Mobile_no = mobile
        user.address = add
        user.city = city
        user.state = state
        user.zipcode = zipcode
        user.save()

        # img=request.POST.get('image')
        # User.objects.filter(username=request.user).update(uname=uname,email=email,address=add,city=city,state=state,zipcode=zipcode)
    context = {'agri_p': agri_p, 'o_agri': o_agri, 'u': u}

    return render(request, 'agri_profile.html', context)


def delete_agri(request,id):
    agri_p = agri.objects.get(id=id)
    agri_p.delete()
    return redirect("/profile/agri_profile")

def update_agri(request,id):
    agri_pro = agri.objects.filter(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        quantity=request.POST.get('Quantity')

        agri.objects.filter(id=id).update(name=name,price=price,quantity=quantity)
        return redirect("/profile/agri_profile")

    return render(request,'update_agri.html',{'agri_pro':agri_pro})


def MYO_profile(request):
    user = request.user
    m_price = add_MarketPrice.objects.all()
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        # mobile=request.POST.get('mbl')
        add = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip_code')

        user = User.objects.get(username=request.user)

        user.uname = uname
        user.email = email
        # user.Mobile_no = mobile
        user.address = add
        user.city = city
        user.state = state
        user.zipcode = zipcode
        user.save()

        # img=request.POST.get('image')
        # User.objects.filter(username=request.user).update(uname=uname,email=email,address=add,city=city,state=state,zipcode=zipcode)
    context = {'m_price': m_price}

    return render(request, 'marketyard_profile.html', context)


def delete_price(request, id):
    m_price = add_MarketPrice.objects.filter(id=id)
    m_price.delete()
    return redirect("/profile/myard_profile")


def update_price(request, id):
    m_price = add_MarketPrice.objects.filter(id=id)
    if request.method == "POST":
        price = request.POST.get('price')

        add_MarketPrice.objects.filter(id=id).update(Price=price)
        return redirect("/profile/myard_profile")

    return render(request, 'update_priceOF_pro.html', {'m_price': m_price})


def farmer_profile(request):
    user = request.user

    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        # mobile=request.POST.get('mbl')
        add = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip_code')

        user = User.objects.get(username=request.user)

        user.uname = uname
        user.email = email
        # user.Mobile_no = mobile
        user.address = add
        user.city = city
        user.state = state
        user.zipcode = zipcode
        user.save()

    return render(request, 'farmer_profile/f_profile.html')


def f_profile(request):
    return render(request, 'farmer_profile/f_profile.html')


def f_crop(request):
    crop_p = crop.objects.all()
    u = User.objects.all()

    o_crop = Order_crop.objects.all()

    context = {'crop_p': crop_p, 'u': u, 'o_crop': o_crop}

    return render(request, 'farmer_profile/f_crop.html', context)


def delete_crop(request, id):
    crop_pro = crop.objects.filter(id=id)
    crop_pro.delete()
    return redirect("/profile/farmer_profile/f_crop")


def update_crop(request, id):
    crop_p = crop.objects.filter(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('Quantity')

        crop.objects.filter(id=id).update(name=name, price=price, quantity=quantity)
        return redirect("/profile/farmer_profile/f_crop")

    return render(request, 'farmer_profile/update_crop_pro.html', {'crop_p': crop_p})


def f_agri(request):
    o_agri = Order_agri.objects.all()

    context = {'o_agri': o_agri}
    return render(request, 'farmer_profile/f_agri.html', context)


def f_machine(request):
    mac = machine.objects.all()
    o_mac = Order_machine.objects.all()
    context = {'mac': mac, 'o_mac': o_mac}
    return render(request, 'farmer_profile/f_machine.html', context)


def delete_machine(request, id):
    m = machine.objects.get(id=id)
    m.delete()
    return redirect("/profile/farmer_profile/f_machine")


def update_machine(request, id):
    mac = machine.objects.filter(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('Quantity')
        key = request.POST.get('key')

        machine.objects.filter(id=id).update(name=name, Approx_price=price, quantity=quantity, key_players=key)
        return redirect("/profile/farmer_profile/f_machine")

    return render(request, 'farmer_profile/update_mac.html', {'mac': mac})





