from django.http.response import HttpResponse
from django.shortcuts import render
from django.apps import apps
from . models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
import ast
from accounts.models import User
import  razorpay


def buy_agri(request):
    categories_agri = Category_agri.get_all_category()
    c_id = request.GET.get('category')
    if c_id:
        products_agri = agri.get_all_products_by_catid(c_id)
    else:
        products_agri = agri.get_all_products()

    data = {'products_agri': products_agri, 'categories_agri': categories_agri}
    return render(request, 'buy_agri.html', data)


def cart_agri(request):
    categories_agri = Category_agri.get_all_category()
    if request.method == "POST":
        userid = request.session['cno']
        item_json = request.POST.get('itemsJson', '')
        item = eval(item_json)
        name = request.POST.get('name', '')
        amount = int(request.POST.get('amount', '')) * 100
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        client = razorpay.Client(auth=("rzp_test_KwMGHCikCcZ1ZJ", "Lzmcdp4FW77SHLmp23rV1jHL"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        order_agri = Order_agri(userid=userid, item_json=item, name=name, amount=amount, email=email, address=address,
                                city=city, state=state, zip_code=zip_code, phone=phone, payment_id=payment['id'])
        order_agri.save()

        thank = True
        id = order_agri.order_id
        return render(request, 'cart_agri.html', {'thank': thank, 'id': id, 'payment': payment})
    return render(request, 'cart_agri.html')


@csrf_exempt
def add_agri(request):
    categories_agri = Category_agri.objects.all()
    cat_name = " "
    c_id = request.GET.get('category')
    if c_id:
        cat_name = Category_agri.get_name_by_catid(c_id)
    else:
        pass

    data = {'categories_agri': categories_agri, 'cat': cat_name}

    if request.method == "POST":
        # try:
        userid = request.session['cno']
        name = request.POST.get('name', '')
        category = request.POST.get('category_id', '')
        company_name = request.POST.get('cname', '')
        price = request.POST.get('price', '')
        image = request.FILES['image']
        quantity = request.POST.get('quantity', '')
        agri(userid=userid, name=name, category=Category_agri(category), company_name=company_name, price=price,
             image=image, quantity=quantity).save()
        messages.success(request, 'Product Added Successfully')

        # except Exception as e:
        #    messages.success(request,'failed to add product')

    return render(request, 'add_agri.html', data)

def success_agri(request):
    if request.method=="POST":
        b=request.POST
        o_id = ""
        for key,value in b.items():
            if key == 'razorpay_order_id':
                o_id=value
        user = Order_agri.objects.filter(payment_id=o_id).first()
        user.paid=True
        print(b)
    return render(request,'success_agri.html')