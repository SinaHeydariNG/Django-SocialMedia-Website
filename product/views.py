from unicodedata import category, decimal
from xmlrpc.client import Boolean
from django.http import HttpResponse
from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from main.models import SiteInfo
from django.core.paginator import Paginator
from .models import Products , Category , Collections , Likes , Comments
from django.db.models import Q
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
from main.models import Navbar
# Create your views here.

def list(request):
    information = SiteInfo.objects.last()
    categories = Category.objects.all()
    collections = Collections.objects.all()
    products = Products.objects.all()
    product_gallery = Products.objects.all().order_by('-published')
    products_values = Products.objects.values_list('type' , flat=True)
    products_count = products.count
    paginator = Paginator(products , 3)
    page =  request.GET.get('page')
    users = CustomUser.objects.all()
    users_paginator = Paginator(users , 20)
    user_page = request.GET.get('page')
    users = users_paginator.get_page(user_page)
    navbars = Navbar.objects.all()
 
    def get_user_price():
        for user in CustomUser.objects.all():
            latest_price = 0
            for price in user.sell.all():                    
                latest_price +=  (price.product_price())         
            return latest_price                                                                        

    print(get_user_price())    
   

    products = paginator.get_page(page)
    context = {
        "information" : information,
        "collections" : collections,
        "categories" : categories,
        "products" : products,
        "product_gallery" : product_gallery,
        "products_count" : products_count,
        "products_values" : products_values,
        "users" : users,
        "navbars" : navbars,
    }

    return render(request , 'products/list.html' , context)
def detail(request , pk):
    information = SiteInfo.objects.last()
    categories = Category.objects.all()
    collections = Collections.objects.all()
    single = get_object_or_404(Products , pk = pk)
    likes = single.likes.count
    products = Products.objects.all()
    products_count = products.count
    paginator = Paginator(products , 3)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    comments = Comments.objects.filter(product = single).order_by('-date')
    users = CustomUser.objects.all()
    navbars = Navbar.objects.all()


    if 'userfilter' in request.GET:
        query = request.GET.get('userfilter')
        if query == "bd":
            users = CustomUser.objects.all().order_by('birthday') 
        elif query == 'like':
            users = CustomUser.objects.all()
        elif query == 'post':
            users = CustomUser.objects.all()   


    context = {
        "information" : information,
        "collections" : collections,
        "categories" : categories,
        "products" : products,
        "products_count" : products_count,
        "single" : single,
        "users" : users,
        "likes" : likes,
        "comments" : comments,
        "navbars" : navbars,        }
    return render(request , 'products/details.html' , context)    


def list_by_category(request , pk):
    information = SiteInfo.objects.last()
    categories = Category.objects.all()
    collections = Collections.objects.all()
    products_values = Products.objects.values_list('type' , flat=True)
    products = Products.objects.filter(category__id = pk).order_by('-published')
    product_gallery = Products.objects.all().order_by('-published')

    products_count = Products.objects.all().count
    paginator = Paginator(products , 3)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    navbars = Navbar.objects.all()
    context = {
        "information" : information,
        "collections" : collections,
        "categories" : categories,
        "products" : products,
        "products_count" : products_count,
        "products_values" : products_values,
        "product_gallery" : product_gallery,
        "navbars" : navbars,

        }      
    return render(request , 'products/list.html' , context)        





def list_by_collection(request , pk):
    information = SiteInfo.objects.last()
    categories = Category.objects.all()
    collections = Collections.objects.all()
    products_values = Products.objects.values_list('type' , flat=True)
    products = Products.objects.all().order_by('-published')
    product_filtered = Products.objects.filter(collection__id = pk)
    product_gallery = Products.objects.all().order_by('-published')
    products_count = Products.objects.all().count
    paginator = Paginator(products , 3)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    navbars = Navbar.objects.all()
    context = {
        "information" : information,
        "collections" : collections,
        "categories" : categories,
        "products" : products,
        "products_count" : products_count,
        "products_values" : products_values,
        "product_filtered" : product_filtered,
        'product_gallery' : product_gallery,
        "navbars" : navbars,

        }      
    return render(request , 'products/list.html' , context) 


def list_by_search(request):
    information = SiteInfo.objects.last()
    categories = Category.objects.all()
    collections = Collections.objects.all()
    products_values = Products.objects.values_list('type' , flat=True)
    product_gallery = Products.objects.all().order_by('-published')
    navbars = Navbar.objects.all()
    if request.method == "GET":
        print("TEST")
        if request.GET.get("Category"):
            category = request.GET.get('Category')
        else:
            category = 0  
        if request.GET.get("collection"):      
            collection = request.GET.get('collection')
        else:
            collection = 0    
        title = request.GET.get('title')
        print(category , collection)
        # if int(category) == 0:
        #     products = Products.objects.all()
        products = Products.objects.filter(
                
                Q(category__id = category) | Q(type = collection) | Q(title__iexact = title)
            )
    products_count = products.count
    paginator = Paginator(products , 3)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    navbars = Navbar.objects.all()
    context = {
        "information" : information,
        "collections" : collections,
        "categories" : categories,
        "products" : products,
        "products_count" : products_count,
        "products_values" : products_values,
        "product_gallery" : product_gallery,
        "navbars" : navbars,

        }
    return render(request , 'products/list.html' , context)        

def likePost(request , pk):
    product = Products.objects.get(pk=pk)
    user = request.user
    if Boolean(Likes.objects.filter(product = product , user = user)) == True:
        print("You cant like this post again :)")
        return redirect("product:detail" , pk = pk)   
    else:
        liked_post = Likes.objects.create(product = product, user = user)
        liked_post.save()  
        return redirect("product:detail" , pk = pk) 

@login_required
def addcomment(request):
    if request.method == "POST":
        user = request.user
        product = request.POST['product'] # Returns the id of that specific product
        get_product = Products.objects.get(id = product)
        pk = get_product.id
        text = request.POST['text']
        new_comment = Comments.objects.create(
            user = user,
            product = get_product,
            text = text,
        )
        new_comment.save()
        return redirect("product:detail" , pk = pk)   
@login_required(login_url='accounts:login')
def create_product(request):
    information = SiteInfo.objects.last()
    collections = Collections.objects.all()
    categories = Category.objects.all()
    user = request.user
    navbars = Navbar.objects.all()
    myform = forms.ProductForm
    if request.method == "POST":
        myform = myform(request.POST , request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect("accounts:profile")
        else:
            messages.error(request , myform.errors)
            return redirect("product:create")  

              
    context = {
        "title" : "Create New",
        "collections" : collections,
        "categories" : categories,
        "information" : information,
        "myform" : myform,
        "navbars" : navbars,
        }
    return render(request , 'products/create.html' , context)   

@login_required()
def delete_product(requset , pk):
    my_product = Products.objects.get(pk = pk)
    my_product.delete()
    return redirect("accounts:profile")

@login_required()
def edit_product(request , pk):
    information = SiteInfo.objects.last()
    collections = Collections.objects.all()
    categories = Category.objects.all()
    single = Products.objects.get(pk = pk)
    navbars = Navbar.objects.all()
    pk = single.id
    if request.method == "POST":
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        type = request.POST['type']
        category = request.POST['category']
        collection = request.POST['collection']
        collection = Collections.objects.get(id = collection)
        category = Category.objects.get(id = category)
        if 'thumbnail' in request.FILES:
            thumbnail = request.FILES['thumbnail']
            single.thumbnail = thumbnail
        information = request.POST['information']
        single.title = title
        single.subtitle = subtitle
        single.type = type
        single.category = category
        single.collection = collection
        single.information = information
        single.save()
        # Products.objects.update(
        # id = pk , title = title , subtitle = subtitle , type = type , category = category , 
        # collection = collection , thumbnail = thumbnail , information = information , owner = request.user
        #  )
        messages.success(request , 'Your product has been updated well :)')
        return redirect("product:edit" , pk=pk)
    context = {
        "title" : "Edit Product",
        "collections" : collections,
        "categories" : categories,
        "information" : information,
        "single" : single,
        "navbars" : navbars,
        }
    return render(request , 'products/edit.html' , context)    