from django.db import models
from djongo import models
from django.contrib.auth.models import AbstractUser

class UserInfo(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=11)


# Create your models here.
