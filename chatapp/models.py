from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manage import CustomUserManager

class CustomUser(AbstractBaseUser):
    phone_number=models.CharField(max_length=10)
    user_profile_image=models.ImageField(upload_to="profile")
    email=models.EmailField(unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    objects = CustomUserManager()
    userid = models.CharField(max_length=100,unique=True)

    USERNAME_FIELD='userid'
    REQUIRED_FIELDS=['email','username']




