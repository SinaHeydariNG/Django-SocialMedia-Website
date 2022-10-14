from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from . import models
from product.models import (Products , Collections , Category)
from django.core.paginator import Paginator
from accounts.models import CustomUser
# Create your views here.

def home(request):
    navbars = models.Navbar.objects.all()
    print(navbars)
    information = models.SiteInfo.objects.last()
    categories = Category.objects.all()
    collections = Collections.objects.all()
    products = Products.objects.all()
    products_count = products.count
    paginator = Paginator(products , 2)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    users = CustomUser.objects.all()

    context = {
        "categories" : categories,
        "collections" : collections,
        "products" : products,
        "products_count" : products_count,
        "information" : information,
        "title" : "Home",
        "navbars" : navbars,
        "users" : users,
        }
    return render(request , 'main/home.html' , context)

def about(request):
    navbars = models.Navbar.objects.all()
    information = models.SiteInfo.objects.last()
    context = {
        "information" : information,
        "title" : "About",
        "navbars" : navbars
        }
    return render(request , 'main/about.html' , context)