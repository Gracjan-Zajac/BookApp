from os.path import isfile
import csv


class Book:

    def __init__(self, name: str, author: str, year: int, genre: str, pages: int, read=False, rate=None):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.read = read
        self.rate = rate

    def __str__(self):
        if self.read:
            return "{}, {}. Year: {}, Genre: {}, Rate: {}".format(self.name, self.author, self.year,
                                                                  self.genre, self.rate)
        else:
            return "{}, {}. Year: {}, Genre: {}, Read: {}".format(self.name, self.author, self.year,
                                                                  self.genre, self.read)

    def __repr__(self):
        return "Book: {}".format(self.name)

    def mark_as_read(self):
        """
        Marking book's status as read.
        """
        self.read = True
        self.rate_book()

    def mark_as_unread(self):
        """
        Marking book's status as unread.
        """
        self.read = False
        self.rate = None

    def rate_book(self, scale=None):
        """
        Rating the book in the scale 1-5
        """
        if scale is None:
            scale = input(f"How did you enjoy {self.name} in the scale from 1 to 5? ")
        else:
            scale = scale
        self.rate = int(scale)


class BooksDatabase:

    def __init__(self, csv_path: str = None):
        self.database_path = csv_path
        self.database = []

        # Load database from disc if possible
        if isfile(self.database_path):
            with open(self.database_path, newline="", encoding="utf-8") as db_file:
                db_reader = csv.reader(db_file)
                next(db_reader)
                self.database = [Book(*book) for book in db_reader]

    def save_db(self):
        pass

# book = Book('Solaris', 'Stanislaw Lem', 1961, 'sci-fi', 340)
# print(book)
# book.mark_as_read()
# print(book)
# book.mark_as_unread()
# print(book)
