from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

def home(request):
    return HttpResponse("helloworld")

def RegisterUser(request):
    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':"something went wrong"})

        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj = Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data,'token':token_obj,'message':'your data has been saved'})
