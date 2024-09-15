from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import generics
from .models import Post
from django.views.generic import (ListView, CreateView, 
                     DeleteView,
                     DetailView, 
                     UpdateView )
from django.views.generic.detail import DetailView
from .serializers import PostSerializer




class PostListView(ListView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
class PostDetailView(DetailView):
  queryset = Post.objects.get('id')
  serializer_class = PostSerializer
  
class PostCreateView(CreateView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
class PostUpdateView(UpdateView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer   
  
class PostDeleteView(DeleteView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer     


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'blog/profile.html')


class 