from django.shortcuts import render
from crop.views import *
from . models import *
# Create your views here.


def add_marketPrice(request):
    categories = Category.objects.all()
    cat_name = " "
    crop_p = " "
    c_id = request.GET.get('category')
    if c_id:
        cat_name = Category.get_name_by_catid(c_id)
        crop_p = crop.get_all_products_by_catid(c_id)
    else:
        pass

    categories = Category.objects.all()
    market_price = add_MarketPrice.objects.all()
    data = {'categories': categories, 'market_price': market_price, 'cat': cat_name, 'crop_product': crop_p}

    if request.method == "POST":
        userid = request.session['cno']
        category = request.POST.get('cat', '')
        Product = request.POST.get('product', '')
        Price = request.POST.get('price', '')
        Yard_name = request.POST.get('yname', '')
        city = request.POST.get('city', '')
        district = request.POST.get('district', '')
        state = request.POST.get('state', '')

        add_MarketPrice(userid=userid, category=Category(category), Product=crop(Product), Price=Price,
                        Yard_name=Yard_name, city=city, district=district, state=state).save()
        messages.success(request, 'price added successfully')
    return render(request, "add_mprice.html", data)


def is_valid_queryparam(param):
    return param != '' and param is not None


def Search_mprice(request):
    crop_pro = crop.objects.all()
    qs = add_MarketPrice.objects.all()
    categories = Category.objects.all()

    category = request.GET.get('category')
    name = request.GET.get('name')
    yname = request.GET.get('yname')
    city = request.GET.get('city')
    district = request.GET.get('District')
    state = request.GET.get('State')
    mindate = request.GET.get('mindate')
    maxdate = request.GET.get('maxdate')

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category__cname=category)

    if is_valid_queryparam(name) and name != 'Choose...':
        qs = qs.filter(Product__name=name)

    if is_valid_queryparam(yname):
        qs = qs.filter(Yard_name=yname)

    if is_valid_queryparam(city):
        qs = qs.filter(city=city)

    if is_valid_queryparam(district):
        qs = qs.filter(district=district)

    if is_valid_queryparam(state):
        qs = qs.filter(state=state)

    if is_valid_queryparam(mindate):
        qs = qs.filter(date__gte=mindate)

    if is_valid_queryparam(maxdate):
        qs = qs.filter(date__lt=maxdate)

    context = {'queryset': qs, 'categories': categories, 'crop_pro': crop_pro}

    return render(request, "search_mprice.html", context)
