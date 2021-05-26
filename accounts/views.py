from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.urls.base import reverse
from .models import User


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        utype = request.POST['users']
        name = request.POST['name']
        mobile = request.POST['mbl']
        pass1 = request.POST['pass']
        add = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST.get('zip_code')
        if User.objects.filter(Mobile_no=mobile).exists():
            messages.info(request, 'Mobile no is registerd already.login.')
            return redirect("accounts:login")
        else:
            user = User.objects.create_user(username=mobile, uname=name, password=pass1, type=utype, address=add,
                                            Mobile_no=mobile, city=city, state=state, zipcode=zipcode)
            user.save()
            messages.info(request, 'Now login to Account')
            return redirect("accounts:login")

    else:
        return render(request, 'signup.html')


def login(request):
    if (request.method == 'POST'):
        pass1 = request.POST['pass']
        mobile = request.POST['name']
        user = auth.authenticate(username=mobile, password=pass1)
        if user is not None:
            auth.login(request, user)
            request.session['cno'] = mobile
            user1 = User.objects.values('type').filter(username=mobile)
            for val in user1:
                if (val['type'] == "Farmer"):
                    return redirect("farmer:home")
                elif (val['type'] == "customer"):
                    return redirect("crop:buy_crop")
                elif (val['type'] == "Agri"):
                    return redirect("agriculture:add_agri")
                elif (val['type'] == "Yard"):
                    return redirect("marketprice:add_marketPrice")
                else:
                    return HttpResponse("Not Found")

        else:
            if User.objects.filter(Mobile_no=mobile).exists():
                messages.info(request, 'Invalid Password.')
                return redirect("accounts:login")
            else:
                messages.info(request, "You haven't registerd yet.")
                return redirect("accounts:register")
    else:
        return render(request, 'signin.html')


def adminlogin(request):
    return redirect("admin_dashboard:home")

