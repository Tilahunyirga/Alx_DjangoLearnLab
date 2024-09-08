
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Create a Book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            published_date="2024-01-01",
            isbn="1234567890123",
            price=25.50
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_date": "2024-02-01",
            "isbn": "9876543210987",
            "price": 30.00
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Including the setUp book
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_update_book(self):
        data = {"title": "Updated Test Book"}
        response = self.client.patch(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.pk).title, "Updated Test Book")

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())


    def test_filter_books(self):
        response = self.client.get(reverse('book-list') + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_search_books(self):
        response = self.client.get(reverse('book-list') + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books(self):
        response = self.client.get(reverse('book-list') + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permissions(self):
        self.client.logout()  # Log out to test unauthenticated access
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Assuming authenticated access is required
