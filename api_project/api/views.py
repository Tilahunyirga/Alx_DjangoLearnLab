from django.shortcuts import render
from rest_framework import generics
from .models import Book
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookListAPIView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializers_class = BookSerializer
  
  
class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer 

class BookViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Only authenticated users can view the list of models
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
