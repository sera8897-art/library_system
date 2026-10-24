class Book:
    """A class to represent a book with a title, author, and borrowing status."""
    total_books = 0  

    def __init__(self, title, author):
        self.title = title          
        self.author = author      
        self.is_borrowed = False     
        Book.total_books += 1

    def __str__(self):
        """Special method to return a string representation of the book object."""
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: '{self.title}' by {self.author} [Status: {status}]"

    def borrow_book(self):
        """Method to borrow the book."""
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Successfully borrowed: '{self.title}'")
        else:
            print(f"Sorry, '{self.title}' is already borrowed!")

    def return_book(self):
        """Method to return the book."""
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Successfully returned: '{self.title}'")
        else:
            print(f"'{self.title}' is already available in the library!")


class Library:
    """A class to represent the library system containing a collection of books."""

    def __init__(self, name):
        self.name = name
        self.books_list = [] 

    def add_book(self, book_obj):
        """Method to add a book to the library catalog."""
        self.books_list.append(book_obj)
        print(f"Added book: '{book_obj.title}' to {self.name}")

    def show_catalog(self):
        """Method to display all books in the library."""
        print(f"\n--- 📚 Catalog of {self.name} ---")

        if not self.books_list:
            print("The library is currently empty.")
        for book in self.books_list:
            print(book)
        print(f"Total Registered Books: {Book.total_books}\n")

    @classmethod
    def library_info(cls):
        """Class method to provide information about the total number of books in the library."""
        return f"Total books in the library system: {Book.total_books}"

    @staticmethod
    def library_rules():
        """Static method to display the library rules."""
        return "Library Rules: 1. Handle books with care. 2. Return books on time. 3. No food or drinks near books."

    