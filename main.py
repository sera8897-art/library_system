from library_system import Book, Library

if __name__ == "__main__":
    print("=== Starting Library Management System ===\n")

    # 1.Create a library instance
    my_library = Library("City University Library")
    print(f"Library Name: {my_library.name}")

    # 2. Update the library name using the setter
    my_library.name = "Central Academic Library"
    print(f"Updated Library Name: {my_library.name}\n")

    # 3. Create book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("Python Crash Course", "Eric Matthes")

    # 4. Add books to the library collection
    my_library.add_book(book1)
    my_library.add_book(book2)

    # 5. Display the library catalog
    my_library.show_catalog()

    # 6. Borrow a book
    book1.borrow_book()
    my_library.show_catalog()

    # 7. Attempt to borrow the same book again
    book1.borrow_book()
    my_library.show_catalog()

    # 8. Return the borrowed book
    book1.return_book()
    my_library.show_catalog()

    # 9. Attempt to return the same book again
    book1.return_book()
    my_library.show_catalog()

    print("\n=== Library Rules ===")
    print(Library.library_rules())

