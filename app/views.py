from django.shortcuts import render
from .serializers import SignUpSerializer,UserSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
import io
from .models import User
from rest_framework.parsers import JSONParser
# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views import View
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.contrib.auth import logout




def home(request):
    return render(request,"delete.html")

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self,request:Request):
        data = request.data
        username = data['username']
        email = data['email']
        print(username)
        print(email)
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
            serializer.save()

            response = {
                "message":"User Created Succesfully",
                "data":serializer.data
            }

            return Response(data=response,status=status.HTTP_200_OK)
        except :
            response = {
                "error":"Error occured"
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(APIView):
    def post(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            # Manually log in the user
            login(request, request.user)
            
            # Retrieve or create the user's authentication token
            token, created = Token.objects.get_or_create(user=request.user)
            
            # Return the updated user information and the token
            data = {
                'user': serializer.data,
                'token': token.key
            }
            return Response(data)
        
        return Response(serializer.errors, status=400)
    
class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # Log out the user
        logout(request)

        # Delete the user
        user.delete()

        return Response({'message': 'User deleted successfully'})