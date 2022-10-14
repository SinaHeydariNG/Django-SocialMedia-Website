from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404 , redirect
from product.models import Products
from .models import Cart , CartItems
# Create your views here.

def add(request , pk):
    product = get_object_or_404(Products , pk=pk)
    user = request.user
    order_product , created = CartItems.objects.get_or_create(
        user = user,
        product = product,
        ordered = False,

    )

    orderCart = Cart.objects.filter(user = request.user , ordered = False)
    if orderCart.exists():
        userOrder = orderCart[0]
        if userOrder.products.filter(product__id = pk ,).exists():
            order_product.quantity += 1
            order_product.save()
            return redirect("accounts:profile")
        else:
            userOrder.products.add(order_product)
            return redirect("accounts:profile")
    else:

        new_order_cart = Cart.objects.create(
            user = user,
            ordered = False
        )
        new_order_cart.products.add(order_product)
        return redirect("accounts:profile")         

def reduce(request , pk):
    product = get_object_or_404(Products , pk=pk)
    user = request.user
    orderCart = Cart.objects.filter(user = request.user , ordered = False)
    if orderCart.exists():
        userOrder = orderCart[0]
        if userOrder.products.filter(product__id = pk ,).exists():
            order_item = CartItems.objects.filter(
                user = user,
                product = product,
                ordered = False,
            )[0]
            if order_item.quantity > 1:
                order_item.quantity  = order_item.quantity -  1
                order_item.save()
                return HttpResponse("Reduced Successfully")
            else:
                order_item.delete()
                return HttpResponse("Deleted Successfully")
        else:
            return HttpResponse("You dont have this item in your cart")
    else:
        return HttpResponse("You dont have an active Cart!")        


def delete(request , pk):
    product = get_object_or_404(Products , pk=pk)
    user = request.user
    orderCart = Cart.objects.filter(user = request.user , ordered = False)
    if orderCart.exists():
        userOrder = orderCart[0]
        if userOrder.products.filter(product__id = pk ,).exists():
            order_item = CartItems.objects.filter(
                user = user,
                product = product,
                ordered = False,
            )[0]
            order_item.delete()
            return HttpResponse("Item deleted Successfully :)")
        else:
            return HttpResponse("You dont have this item in your cart")
    else:
        return HttpResponse("You dont have an active Cart!")        


def checkout(request , pk):
    cart = get_object_or_404(Cart , pk = pk)
    id = cart.id
    user = request.user
    context = {"cart" : id}

    if request.method == "POST":
        address = request.POST['address']
        phone = request.POST['phone']
        cart.address = address
        cart.phone = phone
        cart.ordered = True
        for item in cart.products.all():
            item.ordered = True
            item.save()

        cart.save()
        return HttpResponse("Your request is pending , we will call you as soon as possible to delivere your purchase :)")


    return render(request , 'accounts/checkout.html' , context)

