from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
  post = models.ManyToManyField(Post,)  
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
  
  
class Tag(models.Model):
  name = models.CharField(max_length=100)
  title = models.ManyToManyField(Post, related_name='tag')  