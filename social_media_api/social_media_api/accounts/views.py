from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from django.contrib.auth import login, authenticate
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializers
from rest_framework.generics import( ListCreateAPIView,
                                    RetrieveUpdateAPIView
                                    )
from.models import CustomUser
from rest_framework.authtoken.models import Token


class CustomUserListCreateAPIView(generics.ListCreateAPIView):
  Authentication_class = [TokenAuthentication]
  permission_class = [IsAuthenticated]
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializers
  
  def CustomUser(request):
    username = request.CustomUser("username")
    password = request.CustomUser("password")
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request,user)
      
    else:
      return("create account first")  