from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class UserLevel(models.TextChoices):
    BRONZE = "BRONZE" , "BRONZE"
    SILVER = "SILVER" , "SILVER"
    GOLD = "GOLD" , "GOLD"

class CustomUser(AbstractUser):
    username = models.CharField(max_length=225 , unique=True)
    email = models.EmailField(('email address'), unique=True , )
    image = models.ImageField(upload_to='profile/' , blank = True)
    first_name = models.CharField(max_length=225 , blank=True)
    last_name = models.CharField(max_length=225 , blank=True)
    birthday = models.DateField(blank=True , null=True)
    level = models.CharField(max_length=10 , choices=UserLevel.choices , default=UserLevel.BRONZE)
    following = models.ManyToManyField("self" , blank=True , related_name='followers' , symmetrical=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username