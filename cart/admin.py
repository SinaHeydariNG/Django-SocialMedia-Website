from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CartItems)
admin.site.register(models.Cart)