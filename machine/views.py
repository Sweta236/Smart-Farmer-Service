from django.http.response import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
import ast
from accounts.models import User
import razorpay

def machine_chose(request):
    return render(request, 'machine.html')


# buy Machine

def buy_machine(request):
    categories = Category_Machine.objects.all()
    c_id = request.GET.get('category')
    if c_id:
        products = machine.get_all_products_by_catid(c_id)
    else:
        products = machine.get_all_products()

    data = {'products': products, 'categories': categories}
    return render(request, 'buy_machine.html', data)


def cart_machine(request):
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

        order_machine = Order_machine(userid=userid, item_json=item, name=name, amount=amount, email=email,
                                      address=address, city=city, state=state, zip_code=zip_code, phone=phone,
                                      payment_id=payment['id'])
        print(payment)
        order_machine.save()
        thank = True
        id = order_machine.order_id
        return render(request, 'cart_machine.html', {'thank': thank, 'id': id, 'payment': payment})
    return render(request, 'cart_machine.html')


@csrf_exempt
def add_machine(request):
    categories = Category_Machine.objects.all()
    cat_name = " "
    c_id = request.GET.get('category')
    if c_id:
        cat_name = Category_Machine.get_name_by_catid(c_id)
    else:
        pass

    data = {'categories': categories, 'cat': cat_name}

    if request.method == "POST":
        # try:
        userid = request.session['cno']
        name = request.POST.get('name', '')
        category = request.POST.get('category_id', '')
        Approx_price = request.POST.get('price', '')
        Description = request.POST.get('Description', '')
        image = request.FILES['image']
        quantity = request.POST.get('quantity', '')
        key_players = request.POST.get('key_players', '')
        machine(userid=userid, name=name, category=Category_Machine(category), Approx_price=Approx_price,
                Description=Description, key_players=key_players, image=image, quantity=quantity).save()
        messages.success(request, 'Product Added Successfully')

        # except Exception as e:
        #    messages.success(request,'failed to add product')

    return render(request, 'add_machine.html', data)



def success_mac(request):
    if request.method=="POST":
        c=request.POST
        o_id = ""
        for key,value in c.items():
            if key == 'razorpay_order_id':
                o_id=value
        user = Order_machine.objects.filter(payment_id=o_id).first()
        user.paid=True
        print(c)
    return render(request,'success_mac.html')