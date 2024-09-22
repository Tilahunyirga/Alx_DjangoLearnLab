from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
  author = models.models.ForeignKey(CustomUser , on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
  
  
class Comment(models.Model):
  author = models.ForeignKey(Post, verbose_name=_(""), on_delete=models.CASCADE)
  content = models.TextField(max_length=255) 
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField() 
  