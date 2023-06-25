from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics,status
from rest_framework.request import Request
from django.contrib.auth import authenticate
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
class LoginView(APIView):
    def post(self,request:Request):
        userid = request.data.get('userid')
        password = request.data.get('password')
        email = request.data.get('email')

        user = authenticate(request=None,userid=userid,password=password)
        if user is not None:
            response = {
                "message":"Login Succesfully",
                "token":user.auth_token.key
            }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            response = {
                "message":"In Valid User Id or Password",
            }
            return Response(data=response,status=status.HTTP_404_NOT_FOUND)

    
    def get(self,request:Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }

        return Response(data=content,status=status.HTTP_200_OK)