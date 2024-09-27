# Task 1: Library System Enhancement
# Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

# Existing Library Data:
# ask user to input values for book_name and author


def adding_to_library(library):
    while True:
        book_name = input('\nName of book that you would like to add (or type "exit" to stop): ')
        
        if book_name.lower() == 'exit':
            break
        
        author = input('Author of this book: ')

        whole_book = (book_name, author)
        
        if whole_book in library:
            print("Invalid input: this book already exists.")
        else:
            library.append(whole_book)
            print("\nBook added successfully.")
            print("\nCurrent library:", library)

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

adding_to_library(library)

print("Final library:", library)