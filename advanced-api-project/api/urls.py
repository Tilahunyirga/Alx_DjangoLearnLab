from django.urls import path
from.views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
  path('books/', BookListView.as_view(), name='book_list'),
  path('books/create/', BookCreateView.as_view(), name='book_create'),
  path('books/update', BookUpdateView.as_view(), name='book_update' ),
  path('books/detail/',BookDetailView.as_view(), name='book_retrieve')
  path('books/delete/', BookDeleteView.as_view(), name= 'book_destroy')
]