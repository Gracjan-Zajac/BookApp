import unittest
from main import Book, BooksDatabase


class TestClassBook(unittest.TestCase):

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
        self.my_database = BooksDatabase('test.json')

    def test_add_new_book(self):
        self.my_database.add_new_book('The Trial', 'Franz Kafka', 1925, 'absurd literature', 296)
        self.assertIsInstance(self.my_database.books[0], Book)


if __name__ == '__main__':
    unittest.main()
