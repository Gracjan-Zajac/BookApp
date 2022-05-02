

class Book:
    """
    This class stores information about book.
    """

    def __init__(self, name, author, year, genre, pages, read=False, rate=None):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.read = read
        self.rate = rate
