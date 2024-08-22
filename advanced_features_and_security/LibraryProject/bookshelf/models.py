from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
# Create your models here.
class CustomUser(AbstractUser):
  date_of_birth = models.DateField
  profile_photo =models.ImageField(width_field=10, blank=True)
  
  
class CustomUserManager(BaseUserManager):
  def create_user():
    pass 
  

  def create_superuser():
    pass
  