from itertools import product
from django.db import models
from accounts.models import CustomUser as User
from product.models import Products
# Create your models here.

class CartItems(models.Model):
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sell')
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} from {}".format(self.product , self.user)   

    def product_price(self):
        return self.quantity * self.product.price

 

class OrderStatus(models.TextChoices):
    PENDING = "PENDING" , "PENDING"
    POSTING = "POSTING" , "POSTING"
    DELIEVERED = "DELIEVERED" , "DELIEVERED"

class Cart(models.Model):
    products = models.ManyToManyField(CartItems)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    order_date = models.DateTimeField(blank=True , null=True)
    address = models.CharField(max_length=225 , blank=True , null=True)
    phone = models.CharField(max_length=225 , blank=True , null=True)
    status = models.CharField(max_length=10 , choices=OrderStatus.choices , default=OrderStatus.PENDING)

    def __str__(self):
        return "{}  Cart".format(self.user) 
        

    def total_price(self):
        total = 0
        for product in self.products.all():
            total = total + product.product_price()
        return total
    def total_quantity(self):
        total = 0
        for product in self.products.all():
            total = total + product.quantity     
        return total       

