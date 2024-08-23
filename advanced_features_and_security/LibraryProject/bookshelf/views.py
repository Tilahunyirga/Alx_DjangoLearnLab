from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login 
from django.contrib.auth.models import Group
from .models import post 

def book_list(request):
  book_list = book_list.objects.all()
  return render(request, "bookshelf/book_list.html", {"posts":book_list} )
   

# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)