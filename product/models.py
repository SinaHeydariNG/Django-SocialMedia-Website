from datetime import datetime
from email.policy import default
from weakref import proxy
from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField
# Create your models here.


class FeatureManager(models.Manager):
    def get_queryset(self):
        return super(FeatureManager , self).get_queryset().filter(type = 'f')

class InfographicManager(models.Manager):
    def get_queryset(self):
        return super(InfographicManager , self).get_queryset().filter(type = 'i')

class GalleryManager(models.Manager):
    def get_queryset(self):
        return super(GalleryManager , self).get_queryset().filter(type = 'g')

PRODUCT_TYPES = (
    ('f', 'Feature'),
    ('i', 'Infographic'),
    ('g', 'Gallery'),
)

class Products(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225 , blank=True , null=True)
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE , related_name='product')
    type = models.CharField(max_length=1 , choices=PRODUCT_TYPES ,)
    price = models.DecimalField(max_digits=6 , decimal_places=2 , default=100)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to = 'products/%y/%m/%d' , blank=True)     
    gallery_1 = models.ImageField(upload_to = 'products/%y/%m/%d' , blank=True)     
    gallery_2 = models.ImageField(upload_to = 'products/%y/%m/%d' , blank=True)     
    gallery_3 = models.ImageField(upload_to = 'products/%y/%m/%d' , blank=True)             
    gallery_4 = models.ImageField(upload_to = 'products/%y/%m/%d' , blank=True)     
    collection = models.ForeignKey('Collections' , on_delete=models.PROTECT)
    category = models.ForeignKey('Category' , on_delete=models.PROTECT , related_name='product')
    information = RichTextField(default="TEST")             


class ProductFeatured(Products):
    objects = FeatureManager()
    class Meta:
        proxy = True

class ProductInfographic(Products):
    objects = FeatureManager()
    class Meta:
        proxy = True

class ProductGallery(Products):
    objects = FeatureManager()
    class Meta:
        proxy = True

class Collections(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to = 'colections/%y/%m/%d')
    category = models.ForeignKey('Category' , on_delete=models.CASCADE , default=1 , related_name='collection')

class Category(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to = 'category/%y/%m/%d')


class Likes(models.Model):
    product = models.ForeignKey(Products , on_delete=models.CASCADE , related_name='likes')
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , related_name='likes')


class Comments(models.Model):
    product = models.ForeignKey(Products , on_delete=models.CASCADE , related_name='comments')
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , related_name='comments')
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name='reply' , blank=True , null=True)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    @property
    def childern(self):
        return Comments.objects.filter(parent = self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        else:
            return False        