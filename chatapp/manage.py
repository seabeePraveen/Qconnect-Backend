from typing import Any
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self,userid,password,email,name,**extra_fields):
        if not username:
            raise ValueError("User name Required")
        
        extra_fields['email']=self.normalize_email(extra_fields['email'])
        user=self.model(username=username,email=email,name=name,**extra_fields)
        user.set_password(password)

        user.save(using=self.db)

        return user
    
    def create_user(self,userid,password,email,name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(userid,password,email,name,**extra_fields)
    
    def create_superuser(self,userid,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        return self._create_user(userid,password,**extra_fields)
        
    