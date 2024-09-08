from django.shortcuts import render
from rest_framework.generics import (
  ListAPIView,
  DestroyAPIView,
  CreateAPIView,
  UpdateAPIView,
  RetrieveAPIView
)
from rest_framework import generics
from.models import Book
from.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(generics.ListAPIView):
  queryset =Book.objects.all()
  serializer_class = BookSerializer
  
  def get_queryset(self):
    title = self.kwargs['title']
    author = self.kwargs['author']
    publication_year = self.kwargs['publication_year']
    
    return Book.objects.filter(book_title = title, book_author = author, book_publication_year = publication_year)
  
  
  
class BookDetailView(generics.RetrieveAPIView):
  queryset =Book.objects.all()
  serializer_class = BookSerializer
  lookup_field = 'id'
  
class BookCreateView(generics.CreateAPIView):
  queryset= Book.objects.all()
  serializer_class = BookSerializer 
  permission_classes = [IsAuthenticated] 

class BookUpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class =BookSerializer 
  lookup_field = 'id'
  permission_classes= [IsAuthenticated]
  
class BookDeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class =BookSerializer 
  lookup_field = 'id'
  permission_classes = [IsAuthenticated]
    