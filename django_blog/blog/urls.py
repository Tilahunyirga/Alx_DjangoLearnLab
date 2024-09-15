from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    ...,

    path('/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        ...
]
from . import views

urlpatterns = [
   path('register/', views.register, name='register'),
   path('profile/', views.profile, name='profile'),
]

from .views import (PostCreateView,
                    PostDetailView,
                    PostListView,
                    PostDeleteView,
                    PostUpdateView)

urlpatterns=[
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update')
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/',PostCreateView.as_view(), name= 'post-new')
]

from django.urls import path
from .views import add_comment, CommentEditView, CommentDeleteView

urlpatterns = [
    path('post/<int:post_id>/comments/new/', add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', CommentEditView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
