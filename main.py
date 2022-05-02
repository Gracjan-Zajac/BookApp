class Book:
    """
    This class stores information about book.
    """

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

    def mark_as_read(self):
        """
        Marking book's status as read.
        """
        self.read = True
        self.rate_book()

    def rate_book(self, scale=None):
        """
        Rating the book in the scale 1-5
        """
        if scale is None:
            scale = input(f"How did you enjoy {self.name} in the scale from 1 to 5? ")
        else:
            scale = scale
        self.rate = int(scale)


book = Book('Solaris', 'Stanislaw Lem', 1961, 'sci-fi', 340)
print(book)
book.mark_as_read()
print(book)
