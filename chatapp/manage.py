from typing import Any
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self,userid,password,**extra_fields):
        if not userid:
            raise ValueError("User name Required")
        email = extra_fields.get('email')
        if email is not None:
            email=self.normalize_email(email)
            extra_fields['email']=email
        user=self.model(userid=userid,**extra_fields)
        user.set_password(password)

        user.save(using=self.db)

        return user
    
    def create_user(self,userid,password,**extra_fields):
        return self._create_user(userid,password,**extra_fields)
    
    def create_superuser(self,userid,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        return self._create_user(userid,password,**extra_fields)
        
    