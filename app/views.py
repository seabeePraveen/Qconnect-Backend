from django.shortcuts import render
from .serializers import SignUpSerializer,UserSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
import json
import io
from .models import User,Message
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.contrib.auth import logout





def home(request):
    return render(request,"update.html")

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self,request:Request):
        data = request.data
        username = data['username']
        email = data['email']
        username_exits = User.objects.filter(username=username).exists()
        if username_exits:
            response = {
                "username":"UserName Already exits"
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)

        email_exits = User.objects.filter(email=email).exists()
        if email_exits:
            response = {
                "email":"Email Already exits"
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)


        serializer = self.serializer_class(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            user =serializer.save()
            token_obj,_ = Token.objects.get_or_create(user=user)

            response = {
                "message":"User Created Succesfully",
                "data":serializer.data,
                "token":token_obj.key
            }

            return Response(data=response,status=status.HTTP_200_OK)
        except :
            response = {
                "error":"Error occured"
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(APIView):
    def post(self, request):
        print(request.user)
        data = request.data
        token_old = data['token']
        token_obj = Token.objects.get(key=token_old)
        user = token_obj.user
        if user.email!=data['email']:
            if User.objects.filter(email=data['email']).exists():
                response = {
                    "email":"Email Already exits"
                }
                return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        if user.username!=data['username']:
            if User.objects.filter(username=data['username']).exists():
                response = {
                    "username":"UserName Already exits"
                }
                return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            print("yes serializer is valid")
            user.username = data['username']
            user.email = data['email']
            user.save()
            user = User.objects.get(username=data['username'])
            token_obj,_ = Token.objects.get_or_create(user=user)
            data = {
                'user': serializer.data,
                'token': token_obj.key,
            }
            return Response(data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=400)
    
class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data=request.data
        token=data['token']
        token_obj=Token.objects.get(key=token)
        user=token_obj.user
        

        # Log out the user
        logout(request)

        # Delete the user
        user.delete()

        return Response({'message': 'User deleted successfully'})

class get_user_by_token(APIView):
    def post(self,request):
        data = request.data
        token = data['token']
        
        try:
            token = Token.objects.get(key=token)
            user = token.user
            username = user.username
            email = user.email
            phone_number = user.phone_number
            name = user.name
            return Response(
                {'username': username,
                 'email': email,
                 'phone_number':phone_number,
                 'name':name},status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=400)
        



