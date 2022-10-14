from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Products)
admin.site.register(models.ProductFeatured)
admin.site.register(models.ProductGallery)
admin.site.register(models.ProductInfographic)

admin.site.register(models.Collections)
admin.site.register(models.Category)
admin.site.register(models.Likes)
admin.site.register(models.Comments)