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
print("\n")

class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Формат: {self.format}")


ebook_1 = EBook("Мастер и Маргарита", "Михаил Булгаков", 450, "PDF")
ebook_2 = EBook("Война и мир", "Лев Толстой", 1225, "EPUB")

ebook_1.display_info()
ebook_2.display_info()