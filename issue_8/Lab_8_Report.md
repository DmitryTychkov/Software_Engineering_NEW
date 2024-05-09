# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Тычков Дмитрий Евгеньевич
- ИНО-ОЗБ-ПОАС-22-2

| Задание    | Лаб_раб | Сам_раб |
|------------|---------|---------|
| Задание 1  | +       | +       |
| Задание 2  | +       | +       |
| Задание 3  | +       | +       |
| Задание 4  | +       | +       |
| Задание 5  | +       | +       |
| Задание 6  | +       | +       |
| Задание 7  | +       | +       |
| Задание 8  | +       | +       |
| Задание 9  | -       | -       |
| Задание 10 | -       | -       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- 

## Самостоятельная работа №1
#### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Результат
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages



my_book = Book("Идиот", "Ф.М. Достоевский", 700)
print(my_book.title, my_book.author, my_book.pages)
```
![Меню]()
### Выводы
#### Создаём класс Book с атрибуьами title - название, autor - автор, pages - кол-во страниц. и создаём объект класса Book - my_book.

## Самостоятельная работа №2
#### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Результат
```python
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
```
![Меню]()
### Выводы
#### Добавлен метод display_info - выводит информацию о объекте(книге).

## Самостоятельная работа №3
#### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Результат
```python
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
```
![Меню]()
### Выводы
#### Создаём дочерний класс EBook (Электронная книга). Данный класс наследует методы родителя и расширяет функционал, за счёт того что у класса добавляется новый атрибут, format. Затем создаётся два новых объекта класса EBook и выводятся на экран.

## Самостоятельная работа №4
#### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Результат
```python
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

```
![Меню]()
### Выводы
#### Теперь атрибуты title, author, pages, и format являются приватными, и доступ к ним осуществляется через методы get_title(), get_author(), get_pages(), и get_format().

## Самостоятельная работа №5
#### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Результат
```python
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
```
![Меню]()
### Выводы
####  Метод display_info() в классе EBook предоставляет дополнительную информацию о формате электронной книги, демонстрируя полиморфизм — способность объектов разных классов обеспечивать единый интерфейс через методы с одинаковыми именами.
