# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute, starts as available

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned (available again)."""
        if not self._is_checked_out:
            return False  # Wasn't checked out
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or not available

    def return_book(self, title):
        """Return a book by title (mark as available again)."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or wasn't checked out

    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(book)