from goodreads import GoodReads
from os.path import isfile
import json


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
        self.add_rate()

    def mark_as_unread(self):
        """
        Marks book's status as unread and sets a rate to None.
        """
        self.read = False
        self.rate = None

    def add_rate(self):
        """
        Rates the book in the scale 1-5
        """
        while True:
            scale = int(input(f'How did you enjoy {self.title} in the scale from 1 to 5? '))
            if scale > 5 or scale < 1:
                print('Please rate in the scale from 1 to 5')
            else:
                break

        self.rate = scale

    def print_info(self):
        """
        Prints book's description from GoodReads website.
        """
        book = '{}, {}'.format(self.title, self.author)
        goodreads = GoodReads()
        description = goodreads.get_info(book)
        print(book)
        print('-----')
        print(description)


class BooksDatabase:

    def __init__(self, json_path: str = None):
        self.database_path = json_path
        self.books = []

        # Load database from disc if possible
        if isfile(self.database_path):
            with open(self.database_path, newline='', encoding='utf-8') as db_file:
                db_reader = json.load(db_file)
                self.books = [Book(**book) for book in db_reader]

    def __str__(self):
        return str(self.books)

    def save_db(self):
        """
        Saves books database to json.
        """
        database = json.dumps(self.books, indent=2, default=lambda x: x.__dict__)

        with open(self.database_path, 'w', encoding='utf-8') as db_file:
            db_file.write(database)

    def add_new_book(self):
        """
        Creates a new Book class instance and adds it to the database.
        """
        title = input('Title: ')
        author = input('Author: ')
        year = int(input('Year: '))
        genre = input('Genre: ')
        pages = int(input('Pages: '))

        new_book = Book(title, author, year, genre, pages)
        self.books.append(new_book)

    def count(self):
        """
        Counts how many books and pages user has read.
        """
        books_counter = 0
        pages_counter = 0

        for book in self.books:
            if book.read:
                books_counter += 1
                pages_counter += book.pages

        if books_counter == 0:
            print("You haven't read any book yet.")
        elif books_counter == 1:
            print(f'You have read {books_counter} book with {pages_counter} pages in total. Good job!')
        else:
            print(f'You have read {books_counter} books with {pages_counter} pages in total. Congratulations!')

    def show_read_books(self):
        """
        Prints all books where read = True
        """
        print('Books you have read:')
        for book in self.books:
            if book.read:
                print(f'- {book}')

    def pick_book(self):
        """
        Returns a random book from books where read = False
        """
        pass


db = BooksDatabase('my_books.json')
book = db.books[0]
book.print_info()
