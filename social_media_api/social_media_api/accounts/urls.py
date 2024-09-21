from django.urls import path
from .views import CustomUserListCreateAPIView


urlpatterns = [
  path('accounts/', CustomUserListCreateAPIView.as_view(), name='CustomUser')
]