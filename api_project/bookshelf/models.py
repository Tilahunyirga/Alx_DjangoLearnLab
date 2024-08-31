from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
  date_of_birth = models.DateField
  profile_photo =models.ImageField(width_field=10, blank=True)