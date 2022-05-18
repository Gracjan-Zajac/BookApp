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
    7: 'Count read books',
    8: 'Lucky book',
    9: 'Random quote',
    10: 'Save database',
    11: 'Exit'
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
    try:
        option = int(input('\nSelect an option: '))
    except ValueError:
        print('Invalid option! Please enter a number between 1 and 12\n')
        time.sleep(2)
    else:
        if option == 1:
            print('\nThis is your book collection:\n')
            show_enumerate_books()
            time.sleep(3)
        elif option == 2:
            print('\nWhat book do you want to add?\n')
            details = database.get_book_details()
            database.add_new_book(*details)
            database.save()
            print(f'\n{details[0]} is now added to your list!\n')

            time.sleep(2)
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
                        time.sleep(2)
                        break
                except (ValueError, IndexError):
                    print('Invalid option! Please select a correct number.')
                    time.sleep(2)
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
                            time.sleep(2)
                        else:
                            book.mark_as_read()
                            print(f'{book.title} has been marked as read.\n')
                            time.sleep(2)
                            break
                except (ValueError, IndexError):
                    print('Invalid option! Please select a correct number.')
                    time.sleep(2)
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
                            time.sleep(2)
                            break
                        else:
                            print(f'You have not read {book.title} before.')
                            time.sleep(2)
                except (ValueError, IndexError):
                    print('Invalid option! Please select a correct number.')
                    time.sleep(2)
        elif option == 6:
            while True:
                print("\nWhich book do you want to rate (to quit press '0')?: \n")
                show_enumerate_books()

                try:
                    user_choice = int(input('Your choice: '))
                    if user_choice == 0:
                        break
                    else:
                        book = database.books[user_choice - 1]
                        user_rate = int(input(f'How do you rate {book.title} in the scale from 1 to 5? '))
                        book.add_rate(user_rate)
                        print(f'{book.title} is now rated to {book.rate}\n')
                        time.sleep(2)
                        break
                except (ValueError, IndexError):
                    print('Invalid option! Please select a correct number.')
                    time.sleep(2)
        elif option == 7:
            database.count()
            print('')
            time.sleep(3)
        elif option == 8:
            database.pick_book()
            print('')
            time.sleep(3)
        elif option == 9:
            database.print_quote()
            print('')
            time.sleep(3)
        elif option == 10:
            database.save()
        elif option == 11:
            while True:
                save = input('Do you want to save your database before leaving? [y/n]? ')
                if save.lower() == 'y':
                    database.save()
                    print('\nYour database has been saved!')
                    print('\nSee you again :)')
                    exit()
                elif save.lower() == 'n':
                    print('\nSee you again :)')
                    exit()
                else:
                    print('Invalid option!')
        else:
            print('Invalid option! Please enter a number between 1 and 12\n')
            time.sleep(2)
