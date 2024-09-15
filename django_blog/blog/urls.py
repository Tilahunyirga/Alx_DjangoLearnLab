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

urlpatterns += [
   path('register/', views.register, name='register'),
   path('profile/', views.profile, name='profile'),
]

from .views import (PostCreateView,
                    PostDetailView,
                    PostListView,
                    PostDeleteView,
                    PostUpdateView)

urlpatterns=[
    path('post/<int:pk/>',PostUpdateView.as_view(), name='update')
    path('delete/<int:pk/>', PostDeleteView.as_view(), name="delete"),
    path('create/',PostCreateView.as_view(), name= 'new')
]