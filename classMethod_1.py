# Exercise 1: Class Methods for Counting Instances Instruction:

# Create a class Book with a class variable total_books to count the number of book instances created.
# Implement a class method display_total_books() to display the total number of books created.

class Book:
    _total_books = 0
    _books = []

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book._books.append({
            'title': self.title,
            'author': self.author
        })
        Book._total_books += 1

    @classmethod
    def display_total_books(cls):
        if cls._total_books > 0:
            for index, book in enumerate(cls._books,start=1):
                print(f"\n\nBook No.: {index}\n\nTitle: {book['title']}\nAuthor: {book['author']}")
                
            return(f'\n\n-------------------------------\nTotal number of books: {cls._total_books}\n-------------------------------\n\n')
        else:
            return('No Books in the Store')
    
    

print(Book.display_total_books())

book1 = Book('A boy of gaze','Bob Cliton')
book2 = Book('Dan de lion','Monsiuer Deman')
book3 = Book('Gally of Rose','Hose Maurice')

print(Book.display_total_books())

