class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_pages(self):
        return self.__pages

    def display_info(self):
        print("Книга: ")
        print(f"Название: {self.__title}")
        print(f"Автор: {self.__author}")
        print(f"Кол-во страниц: {self.__pages}")

class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.__format = format

    def display_info(self):
        super().display_info()
        print(f"Формат: {self.__format}")

my_book_1 = Book("Идиот", "Ф.М. Достоевский", 700)
my_book_2 = Book("1984", "Джордж Оруэлл", 565)
ebook_1 = EBook("Мастер и Маргарита", "Михаил Булгаков", 450, "PDF")
ebook_2 = EBook("Война и мир", "Лев Толстой", 1225, "EPUB")

my_book_1.display_info()
my_book_2.display_info()
print("\n")
ebook_1.display_info()
ebook_2.display_info()
print("\n")
# так сработает
print(my_book_1.get_title())
print(ebook_1.get_title())
# а так не сработает
print(my_book_1.__title)
print(ebook_1.__title)
