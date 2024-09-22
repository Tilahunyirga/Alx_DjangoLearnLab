from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet

router = DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('follow/<int:pk>/', FollowViewSet.as_view({'post': 'follow'}), name='follow-user'),
    path('unfollow/<int:pk>/', FollowViewSet.as_view({'post': 'unfollow'}), name='unfollow-user'),
    path("unfollow/<int:user_id>/", FollowViewSet.as_view({''})), 
    path("follow/<int:user_id>")
]
