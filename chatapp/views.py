from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics,status
from rest_framework.request import Request
# Create your views here.

def home(request):
    return render(request,"register.html")




class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self,request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"User Created Succesfully",
                "data": serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)

        response = {
            "message":serializer.errors,
            "data": serializer.data
        }
        
        return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
