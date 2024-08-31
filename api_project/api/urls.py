from django.urls import path, include
from .views import BookListAPIView , BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
  path('api/', include(router.urls)),
  path("books/", BookListAPIView.as_view(), name="book_list_view"),
  ]

