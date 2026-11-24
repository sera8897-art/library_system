from library_system import * 
 
if __name__ == "__main__":
    print("=== Starting Library Management System ===\n")

    # Create a library instance
    my_library = Library("City University Library")
    print(f"Library Name: {my_library.name}")

    # Update the library name using the setter
    my_library.name = "Central Academic Library"
    print(f"Updated Library Name: {my_library.name}\n")

    # Create book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("Python Crash Course", "Eric Matthes")
    book3 = ScienceBook("A Brief History of Time", "Stephen Hawking", "Physics")

    #  Add books to the library collection
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    #find a book by title
    found_book = my_library.find_book("The Great Gatsby")
    if found_book:
        print(f"\nFound book: {found_book}")
    else:
        print("\nBook not found in the library.")

    # Remove a book
    my_library.remove_book(book2) 

    # Display the library catalog
    my_library.show_catalog()

    # Borrow a book
    book1.borrow_book()
    my_library.show_catalog()

    # Attempt to borrow the same book again
    book1.borrow_book()
    my_library.show_catalog()

    # Return the borrowed book
    book1.return_book()
    my_library.show_catalog()

    # Attempt to return the same book again
    book1.return_book()
    my_library.show_catalog()

    # Display total number of books in the library
    print(f"\nTotal books in the library: {Library.get_total_books()}")

    print("\n=== Library Rules ===")
    print(Library.library_rules())


