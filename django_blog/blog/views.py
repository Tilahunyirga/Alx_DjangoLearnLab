from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post
from django.views.generic import (ListView, CreateView, 
                     DeleteView,
                     DetailView, 
                     UpdateView )
from django.views.generic.detail import DetailView
from .serializers import PostSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from requests import Response 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




class PostListView(ListView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
class PostDetailView(DetailView):
  queryset = Post.objects.get('id')
  serializer_class = PostSerializer
  
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author     


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
  
  
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

class CommentEditView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('blog_home')

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
