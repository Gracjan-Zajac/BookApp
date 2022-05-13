import unittest
from main import Book, BooksDatabase


class TestBookMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.book = Book('Solaris', 'Stanislaw Lem', 1964, 'sci-fi', 300)

    def test_marking_as_read(self):
        self.book.mark_as_read()
        self.assertTrue(self.book.read)

    def test_marking_as_unread(self):
        self.book.mark_as_unread()
        self.assertFalse(self.book.read)

    def test_adding_rate(self):
        self.book.add_rate(1)
        self.assertEqual(self.book.rate, 1)
        self.book.add_rate(5)
        self.assertEqual(self.book.rate, 5)


class TestBooksDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.my_books = BooksDatabase('my_books.json')
        self.my_books.books = ['Gracjan']

    def test_deleting_from_database(self):
        self.my_books.books.remove('Gracjan')
        self.assertNotIn('Gracjan', self.my_books.books)


if __name__ == '__main__':
    unittest.main()
