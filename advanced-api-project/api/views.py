from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from.models import Book
from serializers import BookSerializer


class BookListView(generics.ListAPIView):
  queryset =Book.objects.all()
  serializer_class = BookSerializer
  
class BookDetailView(generics.RetrieveAPIView):
  queryset =Book.objects.all()
  serializer_class = BookSerializer
  lookup_field = 'id'
  
class BookCreateView(generics.CreateAPIView):
  queryset= Book.objects.all()
  serializer_class = BookSerializer  

class BookUpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class =BookSerializer 
  lookup_field = 'id'
  
class BookDeleteView(generics.DeleteAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  lookup_field = 'id '