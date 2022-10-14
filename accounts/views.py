from typing import Collection
from django.shortcuts import get_object_or_404, render , get_list_or_404 , redirect
from django.http import HttpResponse
from django.contrib import auth
from .models import CustomUser
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from product.models import (Products , Likes , Comments , Collections , Category)
from main.models import SiteInfo , Navbar
from cart.models import Cart , CartItems
from django.contrib import messages

# Create your views here.

def login(request):
    information = SiteInfo.objects.last()
    products = Products.objects.all()
    products_count = products.count
    navbars = Navbar.objects.all()
    paginator = Paginator(products , 6)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    if request.method ==  "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username , password)
        user = auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request , user)  
            return redirect('accounts:profile')
        else: 
            messages.error(request , 'Wrong username or password')

            return redirect('accounts:login')
    context = {
        "products" : products,
        "products_count" : products_count,
        "information" : information,
        "navbars" : navbars,
        "title" : "Home"
        }
    return render(request , 'accounts/login.html' , context)





def register(request):
    navbars = Navbar.objects.all()
    information = SiteInfo.objects.last()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confrim_password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        image = request.FILES['image']
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request , 'This username has already been taken')
                return redirect('accounts:register')
            elif CustomUser.objects.filter(email=email):
                messages.error(request , 'This email has already been taken')
                return redirect('accounts:register')
            else:
                user = CustomUser.objects.create_user(first_name=first_name , last_name=last_name, username=username, email=email, password=password , image = image , birthday = birthday)    
                auth.login(request , user)
                return redirect('accounts:profile')
    else:
        context = {
        "information" : information,
        "title" : "Register",
        "navbars" : navbars
        }
        return render(request,'accounts/register.html')

@login_required()
def logout(request):
    user = request.user
    auth.logout(request)
    return redirect("accounts:login")



@login_required(login_url='accounts:login')
def profile(request):
    information = SiteInfo.objects.last()
    user = request.user
    products = Products.objects.filter(owner = user)
    products_count = products.count
    navbars = Navbar.objects.all()
    if Cart.objects.filter(user = user , ordered = True).exists():
        user_orders = Cart.objects.filter(user = user , ordered = True)
    else:
        user_orders = None    
    user = request.user
    likes = Likes.objects.filter(product__owner = user).count
    comments = Comments.objects.filter(product__owner = user).count
    cart = Cart.objects.filter(user = user , ordered = False)
    if cart:
        cart = cart[0]
        ordering_list = cart.products.all()
    else:
        cart = None
        ordering_list = None    
    paginator = Paginator(products , 6)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        "products" : products,
        "products_count" : products_count,
        "information" : information,
        "title" : "Home",
        "likes" : likes,
        "comments" : comments,
        "cart" : cart,
        "ordering_list" : ordering_list,
        "user_orders" : user_orders,
        "navbars" : navbars
        }
    return render(request , 'accounts/profile.html' , context)
 
@login_required(login_url='accounts:login')
def user_profile(request , pk):
    navbars = Navbar.objects.all()
    information = SiteInfo.objects.last()
    user = get_object_or_404(CustomUser , pk=pk)
    if request.user.username == user.username:
        return redirect("accounts:profile")
    products = Products.objects.filter(owner = user)
    products_count = products.count   
    likes = Likes.objects.filter(product__owner = user).count
    comments = Comments.objects.filter(product__owner = user).count
    paginator = Paginator(products , 6)
    page =  request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        "user" : user,
        "products" : products,
        "products_count" : products_count,
        "information" : information,
        "title" : "Home",
        "likes" : likes,
        "comments" : comments,
        "navbars" : navbars
        }
    return render(request , 'accounts/profile.html' , context) 


def followToggle(request , pk):
    currentUser = request.user
    activingUser = CustomUser.objects.get(id = pk)
    following = activingUser.followers.all()

    if currentUser != activingUser:
        if currentUser in following:
            activingUser.followers.remove(currentUser)
            return redirect("accounts:user_profile" , pk=activingUser.pk)
        else:
            activingUser.followers.add(currentUser)  
            return redirect("accounts:user_profile" , pk=activingUser.pk) 
    else:
        return redirect("accounts:user_profile" , pk=activingUser.pk)         