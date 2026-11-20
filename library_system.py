
class Book:
    """A class to represent a book."""

    total_books = 0

    def _init_(self, title, author):
        self.__title = title
        self.__author = author
        self.__is_borrowed = False
        Book.total_books += 1

    def get_title(self):
        return self.__title

    def set_title(self, title):
        if self.is_valid_text(title):
            self.__title = title
            return True
        return False

    def get_author(self):
        return self.__author

    def set_author(self, author):
        if self.is_valid_text(author):
            self.__author = author
            return True
        return False

    def get_is_borrowed(self):
        return self.__is_borrowed

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_text(text):
        return isinstance(text, str) and bool(text.strip())

    @property
    def status(self):
        return "Borrowed" if self.__is_borrowed else "Available"

    def _str_(self):
        return f"Book: '{self._title}' by {self._author} [Status: {self.status}]"

    def borrow_book(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"Successfully borrowed: '{self.__title}'")
        else:
            print(f"Sorry, '{self.__title}' is already borrowed!")

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"Successfully returned: '{self.__title}'")
        else:
            print(f"'{self.__title}' is already available in the library!"
class Library: 
    """A class to represent the library system containing a collection of books."""

    def __init__(self, name):
        self._name = name
        self._books_list = [] 

    # getter for name    
    @property
    def name(self):
        return self._name 
       
    # setter for name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def books_list(self):
        return self._books_list

    def add_book(self, book_obj):
        """Method to add a book to the library catalog."""
        self._books_list.append(book_obj)
        print(f"Added book to {self._name}")

    def show_catalog(self):
        """Method to display all books in the library."""
        print(f"\n--- 📚 Catalog of {self._name} ---")

        if not self._books_list:
            print("The library is currently empty.")
        for book in self._books_list:
            print(book)

    @staticmethod
    def library_rules():
        """Static method to display the library rules."""
        return "Library Rules:\n 1. Handle books with care.\n 2. Return books on time.\n 3. No food or drinks near books."
        

    
        

    
