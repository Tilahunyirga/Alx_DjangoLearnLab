from django.shortcuts import render
from rest_framework import generics
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializers_class = BookSerializer
  
  
class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer 



# Create your views here.
