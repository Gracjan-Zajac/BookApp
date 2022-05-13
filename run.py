from main import Book, BooksDatabase

b = BooksDatabase('my_books.json')

menu_options = {
    1: 'Show my books',
    2: 'Add new book',
    3: 'Delete book',
    4: 'Mark as read',
    5: 'Mark as unread',
    6: 'Rate a book',
    7: 'Check book\'s description',
    8: 'Count read books',
    9: 'Lucky book',
    10: 'Random quote',
    11: 'Save database',
    12: 'Exit'
}


def print_menu():
    for key in menu_options.keys():
        print(f'{key}. {menu_options[key]}')


while True:
    print('Welcome in BookApp!\n')
    print_menu()
    option = int(input('\nSelect an option: '))

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass
    elif option == 6:
        pass
    elif option == 7:
        pass
    elif option == 8:
        pass
    elif option == 9:
        pass
    elif option == 10:
        pass
    elif option == 11:
        pass
    elif option == 12:
        print('See you!')
        exit()

# details = b.get_book_details()
# b.add_new_book(details[0], details[1], details[2], details[3], details[4])
