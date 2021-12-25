from django.urls import reverse
#from inventory.views import BookViewSet
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from inventory.models import Book, Author

# Create your tests here.

class TestAll(APITestCase):
    @classmethod
    def setUp(self):
        self.client = APIClient()
        self.factory  = APIRequestFactory()
        self.author = Author.objects.create(
            full_name="Foulen Falten", dob="1998-11-11"
        )
        self.book = Book.objects.create(
            author_field=self.author, title="Tis a book", number_of_pages=100, pages_read = 40
        )
        self.book2 = Book.objects.create(
            author_field=self.author, title="Tis a book with no pages", number_of_pages=0, pages_read = 0
        )
        self.author_url = reverse("authors", args=(self.author.id,))
        self.book_url = reverse("books", args=(self.book.id,))
        self.percentage_url1 = reverse("percentage", args=(self.book.id,))
        self.percentage_url2 = reverse("percentage", args=(self.book2.id,))



    def test_book_get(self):
        response = self.client.get(self.book_url)
        self.assertEquals(response.status_code, 200)

    def test_author_get(self):
        response = self.client.get(self.author_url)
        self.assertEquals(response.status_code, 200)

    def test_get_percentage_ok(self):
        response = self.client.get(self.percentage_url1)
        # self.assertEquals(response.content["percentage"], 40)
        self.assertEquals(response.status_code, 200)

    def test_get_percentage_off(self):
        response = self.client.get(self.percentage_url2)
        self.assertEquals(response.status_code, 403)

