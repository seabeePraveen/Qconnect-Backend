from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username","email","password"]

    def validate(self,attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            return ValidationError("Email has already been Used!")
        
        return super().validate(attrs)