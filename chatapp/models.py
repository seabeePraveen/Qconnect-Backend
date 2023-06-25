from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    username=models.CharField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=10)
    user_profile_image=models.ImageField(upload_to="profile")
    email=models.EmailField(unique=True)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']




