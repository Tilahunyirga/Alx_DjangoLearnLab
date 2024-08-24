from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login 
from django.contrib.auth.models import Group
from .models import Book
from .forms import BookSearchForm

def book_list(request):
  book_list = book_list.objects.all()
  return render(request, "bookshelf/book_list.html", {"posts":book_list} )
   

# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)

# views.py



def search_books(request):
    form = BookSearchForm(request.GET or None)
    if form.is_valid():
        search_term = form.cleaned_data['search_term']
        books = Book.objects.filter(title__icontains=search_term)
    else:
        books = Book.objects.none()
    
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
