import io
from django.shortcuts import render
from .serializers import SignUpSerializer,UserSerializer,MessageSerializer
from rest_framework import generics,status
from rest_framework.request import Request
from .models import User,Message
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views import View
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q




def home(request):
    return render(request,"delete.html")

class LoginView(generics.GenericAPIView):
    def post(self,request:Request):
        data = request.data
        try:
            user = User.objects.get(username=data['username'])
            if user is not None and check_password(data['password'], user.password):
                login(request,user)
                token_obj,_ = Token.objects.get_or_create(user=user)
                response = {
                    "message" : "Login Succesfully",
                    "token" : token_obj.key
                }
                return Response(data=response,status=status.HTTP_200_OK)
            else:
                response = {
                    "error" : "Login Credentials doesn't matched"
                }
                return Response(data=response,status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            response = {
                "error" : "User Doesn't exist"
            }
            return Response(data=response,status=status.HTTP_404_NOT_FOUND)


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

            user.username = data['username']
            user.email = data['email']
            user.name = data['name']
            user.save()
            user = User.objects.get(username=data['username'])
            token_obj,_ = Token.objects.get_or_create(user=user)
            data = {
                'user': serializer.data,
                'token': token_obj.key,
            }
            return Response(data=data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=400)
    
class UserDeleteView(APIView):
    

    def post(self, request):
        data=request.data
        token=data['token']
        #get the details of user using token
        token_obj=Token.objects.get(key=token)
        user=token_obj.user

        # Delete the user
        user.delete()

        return Response({'message': 'User deleted successfully'})

class get_user_by_token(APIView):
    def post(self,request):
        data = request.data
        token = data['token']
        
        try:
        #get the details of user using token
            token = Token.objects.get(key=token)
            user = token.user
            ser = UserSerializer(user)
            return Response(
                ser.data,status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=400)


class get_users_by_starting_string(generics.GenericAPIView):
    def post(self,request):
        data = request.data
        string = data['username']
        users = User.objects.filter(username__startswith=string)
        users_serializer = UserSerializer(users,many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)
        
        return Response(data={"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
    
class get_last_messages_of_user_and_details(generics.GenericAPIView):
    def post(self,request):
        data = request.data
        token = Token.objects.get(key = data['token'])
        current_user = User.objects.get(username=token.user.username)  # Assuming you have authentication in place
        messages = Message.get_messages(self,user=current_user)
        serializer = MessageSerializer(messages,many=True).data
        for data in serializer:
            if data['user'] == data['sender']:
                user = User.objects.get(id = data['receiver'])
                ser = UserSerializer(user).data
                data['user2_pic'] = ser['profile_pic']
                data['user2_username'] = user.username
            else:
                user = User.objects.get(id = data['sender'])
                ser = UserSerializer(user).data
                data['user2_pic'] = ser['profile_pic']
                data['user2_username'] = user.username
        return Response(serializer,status=status.HTTP_200_OK) 