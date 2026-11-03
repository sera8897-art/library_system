class Book:
    """A class to represent a book with a title, author, and borrowing status."""
    total_books = 0  

    def __init__(self, title, author):
        self.__title = title          
        self.__author = author      
        self.__is_borrowed = False     
        Book.total_books += 1

    def _get_title(self):
        return self.__title

    def set_title(self,title):
        if title:
            self.__title=title
     def get_author(self):
         return self.__author

     def set_author(self,author):
         if author:
           self.__author=author

     def get_is_borrowed(self):
         return self.__is_borrowed

    def __str__(self):
        """Special method to return a string representation of the book object."""
        status = "Borrowed" if self.__is_borrowed else "Available"
        return f"Book: '{self.title}' by {self.author} [Status: {status}]"

    def borrow_book(self):
        """Method to borrow the book."""
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"Successfully borrowed: '{self.__title}'")
        else:
            print(f"Sorry, '{self.__title}' is already borrowed!")

    def return_book(self):
        """Method to return the book."""
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"Successfully returned: '{self.__title}'")
        else:
            print(f"'{self.__title}' is already available in the library!")


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
        

    
        

    
