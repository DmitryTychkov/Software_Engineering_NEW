class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages



my_book = Book("Идиот", "Ф.М. Достоевский", 700)
print(my_book.title, my_book.author, my_book.pages)