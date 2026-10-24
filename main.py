from library_system import Book, Library

if __name__ == "__main__":
    print("=== 🚀 Starting Library Management System ===\n")
    my_library = Library("City University Library")

# Create book instances using the constructor
book1 = Book("Clean Code", "Robert Martin")
book2 = Book("Python Crash Course", "Eric Matthes")

# Add books to the library collection
my_library.add_book(book1)
my_library.add_book(book2)

# Display catalog before borrowing
my_library.show_catalog()

#Test borrowing a book
print("--- Borrowing Process ---")
book1.borrow_book()

# Display catalog after borrowing to check status update
my_library.show_catalog()

# Test returning the book
print("--- Returning Process ---")
book1.return_book()

# Display final catalog status
my_library.show_catalog()

print(Library.library_info())
print(Library.library_rules())
