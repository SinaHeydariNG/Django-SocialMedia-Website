from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Following(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    following = models.ForeignKey('self' , on_delete=models.CASCADE)
    
