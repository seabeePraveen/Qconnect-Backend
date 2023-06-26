from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self,request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"User Created Succesfully",
                "data":serializer.data
            }

            return Response(data=response,status=status.HTTP_200_OK)
        else:
            response = {
                "message":serializer.errors
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)

