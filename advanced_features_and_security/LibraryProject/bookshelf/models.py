from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Permission
from django.conf import settings



# Create your models here.
class CustomUser(AbstractUser):
  date_of_birth = models.DateField
  profile_photo =models.ImageField(width_field=10, blank=True)
  
  
class book(models.Model):
  title =models.CharField(max_length=100),
  author = models.CharField(max_length=100) 

class post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, )
  title = models.CharField(max_length=100)    
  class Meta:
    Permissions =[
      ("can_view_Book","can view book" ),
      ("can_create_Book", "can create book"),
      ("can_edit_Book", "can edit book"),
      ("can_delete_Book", "can delete book")
      
    ]
  
  
class CustomUserManager(BaseUserManager):
  def create_user():
    pass 
  

  def create_superuser():
    pass
  
  