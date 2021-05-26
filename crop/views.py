from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.apps import apps
from . models import *
from django.contrib.auth.models import auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
import ast
from accounts.models import User
import razorpay


def buy_crop(request):
    categories = Category.get_all_category()
    c_id = request.GET.get('category')
    if c_id:
        products = crop.get_all_products_by_catid(c_id)
    else:
        products = crop.get_all_products()

    data = {'products': products, 'categories': categories}
    return render(request, 'buy_crop.html', data)


def cart_crop(request):
    if request.method == "POST":
        userid = request.session['cno']
        item_json = request.POST.get('itemsJson', '')
        item = eval(item_json)
        name = request.POST.get('name', '')
        amount = int(request.POST.get('amount', '')) * 100
        email = request.POST.get('email', '')
        address = request.POST.get('address')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        client = razorpay.Client(auth=("rzp_test_KwMGHCikCcZ1ZJ", "Lzmcdp4FW77SHLmp23rV1jHL"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        order = Order_crop(userid=userid, item_json=item, name=name, amount=amount, email=email, address=address,
                           city=city, state=state, zip_code=zip_code, phone=phone, payment_id=payment['id'])
        print(payment)
        order.save()

        thank = True
        id = order.order_id
        return render(request, 'cart_crop.html', {'thank': thank, 'id': id, 'payment': payment})
    return render(request, 'cart_crop.html')


@csrf_exempt
def add_crop(request):
    categories = Category.objects.all()
    cat_name = " "
    c_id = request.GET.get('category')
    if c_id:
        cat_name = Category.get_name_by_catid(c_id)
    else:
        pass

    data = {'categories': categories, 'cat': cat_name}

    if request.method == "POST":
        # try:
        userid = request.session['cno']
        name = request.POST.get('name', '')
        category = request.POST.get('category_id', '')
        price = request.POST.get('price', '')
        image = request.FILES['image']
        quantity = request.POST.get('quantity', '')
        crop(userid=userid, name=name, category=Category(category), price=price, image=image, quantity=quantity).save()
        messages.success(request, 'Product Added Successfully')

        # except Exception as e:
        #    messages.success(request,'failed to add product')

    return render(request, 'add_crop.html', data)

def success_c(request):
    if request.method=="POST":
        a=request.POST
        o_id = ""
        for key,value in a.items():
            if key == 'razorpay_order_id':
                o_id=value
        user = Order_crop.objects.filter(payment_id=o_id).first()
        user.paid=True
        print(a)
    return render(request,'success_c.html')