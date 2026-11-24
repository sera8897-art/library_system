class Book:
    """A class to represent a book."""
    total_books = 0

    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._is_borrowed = False
        Book.total_books += 1

    # getter and setter for title 
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and bool(new_title.strip()):
            self._title = new_title
            return True
        return False
    
    # getter and setter for author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, str) and bool(new_author.strip()):
            self._author = new_author
            return True
        return False
    
    # getter for is_borrowed returns True if the book is borrowed, False otherwise
    @property
    def is_borrowed(self):
        return self._is_borrowed

    # status property returns "Borrowed" if the book is borrowed, "Available" otherwise
    @property
    def status(self):
        return "Borrowed" if self._is_borrowed else "Available"

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def __str__(self):
        return f"Book: '{self._title}' by {self._author} [Status: {self.status}]"

    def borrow_book(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            print(f"Successfully borrowed: '{self._title}'")
        else:
            print(f"Sorry, '{self._title}' is already borrowed!")

    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            print(f"Successfully returned: '{self._title}'")
        else:
            print(f"'{self._title}' is already available in the library!")

class ScienceBook(Book):
    """A subclass of Book specifically for science books."""
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self._subject = subject

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject):
        if isinstance(new_subject, str) and bool(new_subject.strip()):
            self._subject = new_subject
            return True
        return False

    def __str__(self):
        return f"Science Book: '{self.title}' by {self.author} [Subject: {self.subject}] [Status: {self.status}]"

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

    def remove_book(self, book_obj):
        """Method to remove a book from the library catalog."""
        if book_obj in self._books_list:
            self._books_list.remove(book_obj)
            print(f"Removed book from {self._name}")
        else:
            print(f"Book not found in {self._name}")    

    def find_book(self, title):
        """Method to find a book by title in the library catalog."""
        for book in self._books_list:
            if book.title == title:
                return book
        return None            

    def show_catalog(self):
        """Method to display all books in the library."""
        print(f"\n--- 📚 Catalog of {self._name} ---")

        if not self._books_list:
            print("The library is currently empty.")
        else:
            for book in self._books_list:
                print(book)

    def __str__(self):
        return f"Library: {self._name} with {len(self._books_list)} books."
        
    @staticmethod
    def library_rules():
        """Static method to display the library rules."""
        return "Library Rules:\n 1. Handle books with care.\n 2. Return books on time.\n 3. No food or drinks near books."

