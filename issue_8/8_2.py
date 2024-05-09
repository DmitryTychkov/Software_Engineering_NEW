class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_info(self):
        print("Книга: ")
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Кол-во страниц: {self.pages}")


my_book_1 = Book("Идиот", "Ф.М. Достоевский", 700)
my_book_2 = Book("1984", "Джордж Оруэлл", 565)

my_book_1.display_info()
my_book_2.display_info()
