from django.db import models
from django.contrib.auth.models import AbstractUser
import random 

class User(AbstractUser):
    phone = models.CharField(max_length=13)
    
    def __str__(self):
        return self.phone

class CheckCode(models.Model):
    code = models.CharField(max_length=4)