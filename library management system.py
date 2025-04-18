class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = 'Available' if self.is_available else 'Not Available'
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!\n")

    def display_books(self):
        print("Available Books:")
        for idx, book in enumerate(self.books):
            if book.is_available:
                print(f"{idx + 1}. {book}")
        print("\n")

    def lend_book(self, book_title, customer):
        for book in self.books:
            if book.title.lower() == book_title.lower() and book.is_available:
                book.is_available = False
                self.borrowed_books.append((book, customer))
                print(f"'{book.title}' has been borrowed by {customer.name}.\n")
                return
        print("Sorry, the book is either not available or doesn't exist.\n")

    def return_book(self, book_title, customer):
        for borrowed_book, borrower in self.borrowed_books:
            if borrowed_book.title.lower() == book_title.lower() and borrower == customer:
                borrowed_book.is_available = True
                self.borrowed_books.remove((borrowed_book, borrower))
                print(f"'{borrowed_book.title}' has been returned by {customer.name}.\n")
                return
        print("The book return failed. Please check details.\n")

    def display_borrowed_books(self):
        print("Borrowed Books:")
        for book, customer in self.borrowed_books:
            print(f"{book.title} - Borrowed by {customer.name}")
        print("\n")


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Customer(User):
    def borrow_book(self, library, book_title):
        library.lend_book(book_title, self)

    def return_book(self, library, book_title):
        library.return_book(book_title, self)


class Admin(User):
    def add_book(self, library, title, author):
        new_book = Book(title, author)
        library.add_book(new_book)

    def view_borrowed_books(self, library):
        library.display_borrowed_books()


# Main Function to Simulate Library System
def main():
    library = Library()

    # Admin adding books
    admin = Admin("Librarian")
    admin.add_book(library, "The Alchemist", "Paulo Coelho")
    admin.add_book(library, "1984", "George Orwell")
    admin.add_book(library, "To Kill a Mockingbird", "Harper Lee")

    # Display available books
    library.display_books()

    # Customers borrowing books
    customer1 = Customer("Ram")
    customer2 = Customer("Sara")
    customer1.borrow_book(library, "1984")
    customer2.borrow_book(library, "The Alchemist")

    # Display borrowed books
    admin.view_borrowed_books(library)
    library.display_books()

    # Returning books
    customer1.return_book(library, "1984")
    library.display_books()
    admin.view_borrowed_books(library)


if __name__ == "__main__":
    main()

