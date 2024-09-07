from rest_framework import serializers
from .models import Book
from .models import Author
import datetime

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id', 'name']   
  


class BookSerializer(serializers.ModelSerializer):
  author = serializers.CharField(many=True, read_only =True)
  class Meta:
    model = Book
    fields ='__all__'
    
    def validate(self, data):
      if data['publication_year'] > datetime.date.today():
        raise serializers.ValidationError("not found")
    
    

