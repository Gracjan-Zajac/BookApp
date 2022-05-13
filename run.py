from main import Book, BooksDatabase

b = BooksDatabase('my_books.json')

menu_options = {
    1: 'Show my books',
    2: 'Add new book',
}


def print_menu():
    for key in menu_options.keys():
        print(f'{key}. {menu_options[key]}')

print_menu()

# while True:
#     pass
    # details = b.get_book_details()
    # b.add_new_book(details[0], details[1], details[2], details[3], details[4])
