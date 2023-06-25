from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['userid','password','email','phone_number']

    def validate(self,attrs):
        email_exists = CustomUser.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email has already in Use")

        return super().validate(attrs)
        
    def create(self,validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user

    

