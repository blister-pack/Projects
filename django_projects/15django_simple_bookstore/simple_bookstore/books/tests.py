from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book

# Create your tests here.


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="testuser", password="testpass")
        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            description="A book about a wizard",
            published_date="2000-01-01",
            price=25.00,
        )

    # CRUD TESTS
    # Create
    def test_book_creation(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.author, "JK Rowling")
        self.assertEqual(self.book.description, "A book about a wizard")
        self.assertEqual(self.book.published_date, "2000-01-01")
        self.assertEqual(self.book.price, 25.00)

    # Read
    def test_book_retrieval(self):
        book_from_db = Book.objects.get(pk=self.book.pk)
        self.assertEqual(book_from_db, self.book)

    # Update
    def test_book_update(self):
        self.book.title = "An updated title"
        self.book.save()
        self.assertEqual(self.book.title, "An updated title")

    # Delete
    def test_book_deletion(self):
        book_id = self.book.id
        self.book.delete()
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)

    def test_str_representation(self):
        self.assertEqual(self.book.__str__(), "Harry Potter")

    def test_book_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), f"/books/{self.book.pk}/")
