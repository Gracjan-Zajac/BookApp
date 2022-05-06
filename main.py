from os.path import isfile
import csv


class Book:

    def __init__(self, title: str, author: str, year: int, genre: str, pages: int, read=False, rate=None):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.read = read
        self.rate = rate

    def __str__(self):
        if self.read:
            return '{}, {}. Year: {}, Genre: {}, Rate: {}'.format(self.title, self.author, self.year,
                                                                  self.genre, self.rate)
        else:
            return '{}, {}. Year: {}, Genre: {}, Read: {}'.format(self.title, self.author, self.year,
                                                                  self.genre, self.read)

    def __repr__(self):
        return 'Book: {}'.format(self.title)

    def __iter__(self):
        return iter([self.title, self.author, self.year, self.genre, self.pages, self.read, self.rate])

    def mark_as_read(self):
        """
        Marks book's status as read and moves to rate_book function.
        """
        self.read = True
        self.rate_book()

    def mark_as_unread(self):
        """
        Marks book's status as unread and sets a rate to None.
        """
        self.read = False
        self.rate = None

    def rate_book(self, scale=None):
        """
        Rates the book in the scale 1-5
        """
        if scale is None:
            scale = input(f'How did you enjoy {self.title} in the scale from 1 to 5? ')
        else:
            scale = scale
        self.rate = int(scale)


class BooksDatabase:

    def __init__(self, csv_path: str = None):
        self.database_path = csv_path
        self.database = []

        # Load database from disc if possible
        if isfile(self.database_path):
            with open(self.database_path, newline='', encoding='utf-8') as db_file:
                db_reader = csv.reader(db_file)
                next(db_reader)
                self.database = [Book(*book) for book in db_reader]

    def __str__(self):
        return str(self.database)

    def save_db(self):
        """
        Saves books database to csv.
        """
        header = ['Title', 'Author', 'Year', 'Genre', 'Pages', 'Read', 'Rate (1-5)']
        with open(self.database_path, 'w', newline='', encoding='utf-8') as db_file:
            db_writer = csv.writer(db_file)
            db_writer.writerow(header)
            for book in self.database:
                db_writer.writerow(book)

    def add_new_book(self, title=input('Title: '), author=input('Author: '), year=int(input('Year: ')),
                     genre=input('Genre: '), pages=int(input('Pages: '))):
        """
        Creates a new Book class instance and adds it to the database.
        """
        new_book = Book(title, author, year, genre, pages)
        self.database.append(new_book)

    def count(self):
        """
        Counts how many books and pages user has read.
        """
        pass


db = BooksDatabase('my_books.csv')
db.add_new_book()
db.save_db()

