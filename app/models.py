from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password,**extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_admin',True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super User hs to have is_staff being True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super User hs to have is_superuser being True")

        return self.create_user(username=username,email=email,password=password,**extra_fields)



class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    objects = CustomUserManager()
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True