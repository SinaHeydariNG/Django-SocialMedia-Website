from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    logo = models.ImageField(upload_to = 'logo/%y/%m/%d')
    phone = models.CharField(max_length=225)
    email = models.EmailField()
    location = models.CharField(max_length=225)
    about = RichTextField()
    copyright = models.CharField(max_length=225)

    class Meta:
        verbose_name = "Information"

    def __str__(self):
        return "YOUR WEBSITE INFO IS HERE :)" 
       

class Navbar(models.Model):
    title = models.CharField(max_length=225)
    url = models.URLField()

    def __str__(self):
        return self.title 
