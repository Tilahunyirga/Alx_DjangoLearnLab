from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
  bio = models.TextField(blank=True)
  profile_picture = models.ImageField(null=True)
  followers  = models.ManyToManyField(symmetrical=False)
  
  