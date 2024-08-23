from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Permission




# Create your models here.
class CustomUser(AbstractUser):
  date_of_birth = models.DateField
  profile_photo =models.ImageField(width_field=10, blank=True)
  
  class meta:
    Permissions =[
      ("can_view","can view" ),
      ("can_create", "can create"),
      ("can_edit", "can edit"),
      ("can_delete", "can delete")
      
    ]
  
  
class CustomUserManager(BaseUserManager):
  def create_user():
    pass 
  

  def create_superuser():
    pass
  
  