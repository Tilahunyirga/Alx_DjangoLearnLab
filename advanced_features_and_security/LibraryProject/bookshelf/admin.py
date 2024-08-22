from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin, CustomUser

# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)