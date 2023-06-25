from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
# Create your views here.

def home(request):
    return render(request,"register.html")

class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

