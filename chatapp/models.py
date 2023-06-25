from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manage import CustomUserManager

class CustomUser(AbstractBaseUser):
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    user_profile_image=models.ImageField(upload_to="profile",null=True)
    email=models.EmailField(unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    objects = CustomUserManager()
    userid = models.CharField(max_length=100,unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD='userid'
    REQUIRED_FIELDS=['email']


    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser



