from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import GoodsType, GoodsCategory, Good, Cart, gComment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime

def index(request,gType="",gCat=""):
    data={
        "types": get_types(), 
        "cats": get_categotyes(gType), 
        "goods": get_goods(gType,gCat), 
        "currentType": gType,
        "cartCount": cart_count(request.user)
        }
    return render(request,"index.html",context=data)

def show_good(request, gType="",gCat="", goodId=""):
    if request.method == 'POST':
        add_good_comment(goodId, request.POST.get("comment"), request.user)
    data={
        "good": get_one_good(goodId), 
        "comments": get_good_comments(goodId),
        "cartCount": cart_count(request.user)        
        }
    return render(request,"good.html",context=data)

def site_authorization(request):
    variant = request.POST.get("variant")
    if variant=="login":
        user = authenticate(request, username=request.POST.get("name"), password=request.POST.get("pass"))
        if user is None:
            return HttpResponse("Login invalid, no user found or bad password!")
    elif variant=="register":
        try:
            user = User.objects.create_user(request.POST.get("name"), 'test@nomail.com', request.POST.get("pass"))
        except:
            return HttpResponse("Register failed, try another name!")
    login(request, user)
    return HttpResponseRedirect("/")

def site_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def cart_show(request):
    data={
        "carts": get_cart_goods(request.user),
        "cart_sum": cart_calculate(request.user),
        "cartCount": cart_count(request.user)        
        }
    return render(request,"cart.html",context=data)    

def cart_add(request,goodId):
    good = get_one_good(goodId);
    Cart.objects.get_or_create(linkU=request.user, linkG=good, price=good.price)
    return HttpResponseRedirect("/cart")

def cart_delete(request,goodId):
    Cart.objects.filter(linkU=request.user, linkG__id=goodId).delete()
    return HttpResponseRedirect("/cart")

def cart_clear(request):
    Cart.objects.filter(linkU=request.user).delete()
    return HttpResponseRedirect("/cart")

def make_order(request):
    return HttpResponse("Thanks you! Please pay <b>"+cart_calculate(request.user)+"</b> to us.")

#------------------------------------------------------------------

def get_types(): # тут все типы
    types = GoodsType.objects.all()
    return types

def get_categotyes(gType): # категории по типу
    if gType=="":
        cats = [] #GoodsCategory.objects.all()
    else:
        cats = GoodsCategory.objects.filter(linkT__addr=gType)
    return cats

def get_goods(gType,gCat): # все товары по отборам
    if gType=="":
        goods = Good.objects.all()
    elif gCat=="":
        goods = Good.objects.filter(linkT__addr=gType)
    else:
        goods = Good.objects.filter(linkT__addr=gType,linkC__addr=gCat)
    return goods

def get_one_good(goodId): # получить карточку товара
    return Good.objects.get(id=goodId)

def get_good_comments(goodId): # получить комментарии по товару
    return gComment.objects.filter(linkG__id=goodId)

def add_good_comment(goodId, comment, user):
    good = get_one_good(goodId);
    now = datetime.now()
    gComment.objects.create(linkU=user, dateAdded=now,comment=comment,linkG=good)

def get_cart_goods(user):
    return Cart.objects.filter(linkU=user)

def cart_calculate(user):
    db_req = Cart.objects.filter(linkU=user).aggregate(total=Sum("price"))
    total = db_req["total"];
    if total is None:
        sum_order = "$ 0"
    else:
        sum_order = "$ {:14.2f}".format(total)
    return sum_order

def cart_count(user):
    if not user.is_authenticated:
        return 0
    else:
        return Cart.objects.filter(linkU=user).count()
