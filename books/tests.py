from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookTest(TestCase):
    ''' Testing Book model '''
    def setUp(self):
        self.user = User.objects.create_user(username = 'momo',
            email='momo@momo.com',
            password='momo')
        self.author = Author.objects.create(
            first_name='Test',
            last_name='Author')
        self.test_book = Book(
            title="Test Book",
            author=self.author,
            user=self.user,
            genre="Test Genre",
            owned=True,
            to_read=False
            )
        self.test_book.save()

    def test_book_retrieval(self):
        '''Tests whether we can retrieve an added book.'''
        retrieved_book = Book.objects.get(title="Test Book")
        self.assertEqual(retrieved_book.user.username, 'momo')
        self.assertEqual(retrieved_book.user.email, 'momo@momo.com')
        self.assertEqual(retrieved_book.author.first_name, "Test")
        self.assertEqual(retrieved_book.author.last_name, "Author")
        self.assertEqual(retrieved_book.genre, "Test Genre")
        self.assertEqual(retrieved_book.owned, True)
        self.assertEqual(retrieved_book.to_read, False)


