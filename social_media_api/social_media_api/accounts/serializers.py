from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate


class CustomUserSerializers(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = __all__
    
    