from main import BooksDatabase
import time

database = BooksDatabase('my_books.json')

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


def show_enumerate_books():
    for count, book in enumerate(database.books):
        print(f'{count + 1}. {book}\n')


while True:
    print('This is BookApp!\n')
    print_menu()
    option = int(input('\nSelect an option: '))

    if option == 1:
        print('\nThis is your book collection:\n')
        show_enumerate_books()
        time.sleep(3)

    elif option == 2:
        print('\nWhat book do you want to add?\n')
        details = database.get_book_details()
        database.add_new_book(*details)
        print(f'\n{details[0]} is now added to your list!\n')

        time.sleep(3)

    elif option == 3:
        while True:
            print("\nWhich book do you want to delete (to quit press '0'): \n")
            show_enumerate_books()
            try:
                user_choice = int(input('Your choice: '))
                if user_choice == 0:
                    break
                elif user_choice != 0:
                    book_to_delete = database.books[user_choice - 1]
                    print(f'{book_to_delete.title} has been deleted!\n')
                    database.books.remove(book_to_delete)
                    time.sleep(3)
                    break
            except ValueError:
                print('Invalid option! Please select a correct number.')
                time.sleep(3)

    elif option == 4:
        while True:
            print("\nWhich book did you finished reading (to quit press '0')?: \n")
            show_enumerate_books()
            try:
                user_choice = int(input('Your choice: '))
                if user_choice == 0:
                    break
                elif user_choice != 0:
                    book = database.books[user_choice - 1]
                    if book.read:
                        print(f'You have read {book.title} before.')
                        time.sleep(3)
                    else:
                        book.mark_as_read()
                        print(f'{book.title} has been marked as read.\n')
                        time.sleep(3)
                        break
            except ValueError:
                print('Invalid option! Please select a correct number.')
                time.sleep(3)

    elif option == 5:
        while True:
            print("\nWhich book do you want to mark as unread (to quit press '0')?: \n")
            show_enumerate_books()
            try:
                user_choice = int(input('Your choice: '))
                if user_choice == 0:
                    break
                elif user_choice != 0:
                    book = database.books[user_choice - 1]
                    if book.read:
                        book.mark_as_unread()
                        print(f'{book.title} has been marked as unread.\n')
                        time.sleep(3)
                        break
                    else:
                        print(f'You have not read {book.title} before.')
                        time.sleep(3)
            except ValueError:
                print('Invalid option! Please select a correct number.')
                time.sleep(3)

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
        print('\nSee you again!')
        exit()
    else:
        print('Invalid option! Please enter a number between 1 and 12')

# details = b.get_book_details()
# b.add_new_book(details[0], details[1], details[2], details[3], details[4])
