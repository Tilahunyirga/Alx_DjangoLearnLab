from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login 
from django.contrib.auth.models import Group
from .models import Book
from .forms import ExampleForm

def book_list(request):
  book_list = book_list.objects.all()
  return render(request, "bookshelf/book_list.html", {"posts":book_list} )
   

# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)



def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # For now, just print it to the console or handle as needed
            print(f"Name: {name}, Email: {email}, Message: {message}")
            # Optionally redirect to a new URL or render a success message
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
