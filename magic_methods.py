class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages
    
    # def __str__(self):
    #     return(f'{self.author},{self.pages},{self.title}')
    
    def __repr__(self):
        return(f"Book(author = '{self.author}', title = '{self.title}', pages = {self.pages})")
        

book1 = Book('Charles Darkins', 'We did okay kid', 300)

print(book1)