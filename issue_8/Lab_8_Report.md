# ���� 8. �������� � ���
����� �� ���� #8 ��������(�):
- ������ ������� ����������
- ���-���-����-22-2

| �������    | ���_��� | ���_��� |
|------------|---------|---------|
| ������� 1  | +       | +       |
| ������� 2  | +       | +       |
| ������� 3  | +       | +       |
| ������� 4  | +       | +       |
| ������� 5  | +       | +       |
| ������� 6  | +       | +       |
| ������� 7  | +       | +       |
| ������� 8  | +       | +       |
| ������� 9  | -       | -       |
| ������� 10 | -       | -       |

���� "+" - ������� ���������; ���� "-" - ������� �� ���������;

������ ���������:
- 

## ��������������� ������ �1
#### �������������� �������� ����� � ��� ������. ��� ������ ����������, �� ���, ��� ������� � ������������� ��������� (���������) � ������������ ��������. ����������� ���������� ������� ����� ������� ���� � ������������ ����� �������.

### ���������
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages



my_book = Book("�����", "�.�. �����������", 700)
print(my_book.title, my_book.author, my_book.pages)
```
![����]()
### ������
#### ������ ����� Book � ���������� title - ��������, autor - �����, pages - ���-�� �������. � ������ ������ ������ Book - my_book.

## ��������������� ������ �2
#### �������������� �������� �������� � ������ ��� ����� ���������� ������. ��� ������ ����������, �� ���, ��� ������� � ������������� ��������� (���������) � ������������ ��������. ����������� ���������� ������� ����� ������� ���� � ������������ ����� �������.

### ���������
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_info(self):
        print("�����: ")
        print(f"��������: {self.title}")
        print(f"�����: {self.author}")
        print(f"���-�� �������: {self.pages}")


my_book_1 = Book("�����", "�.�. �����������", 700)
my_book_2 = Book("1984", "������ ������", 565)

my_book_1.display_info()
my_book_2.display_info()
```
![����]()
### ������
#### �������� ����� display_info - ������� ���������� � �������(�����).

## ��������������� ������ �3
#### �������������� ���������� ������������, ��������� �������� � ����� ��������� �������. ��� ������ ����������, �� ����, ��� ������� � ������������� ��������� (���������) � ������������ ��������. ����������� ���������� ������� ����� ������� ���� � ������������ ����� �������.

### ���������
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_info(self):
        print("�����: ")
        print(f"��������: {self.title}")
        print(f"�����: {self.author}")
        print(f"���-�� �������: {self.pages}")


my_book_1 = Book("�����", "�.�. �����������", 700)
my_book_2 = Book("1984", "������ ������", 565)

my_book_1.display_info()
my_book_2.display_info()
print("\n")

class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"������: {self.format}")


ebook_1 = EBook("������ � ���������", "������ ��������", 450, "PDF")
ebook_2 = EBook("����� � ���", "��� �������", 1225, "EPUB")

ebook_1.display_info()
ebook_2.display_info()
```
![����]()
### ������
#### ������ �������� ����� EBook (����������� �����). ������ ����� ��������� ������ �������� � ��������� ����������, �� ���� ���� ��� � ������ ����������� ����� �������, format. ����� �������� ��� ����� ������� ������ EBook � ��������� �� �����.

## ��������������� ������ �4
#### �������������� ���������� ������������, ��������� �������� � ����� ��������� �������. ��� ������ ����������, �� ����, ��� ������� � ������������� ��������� (���������) � ������������ ��������. ����������� ���������� ������� ����� ������� ���� � ������������ ����� �������.

### ���������
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
        print("�����: ")
        print(f"��������: {self.__title}")
        print(f"�����: {self.__author}")
        print(f"���-�� �������: {self.__pages}")

class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.__format = format

    def display_info(self):
        super().display_info()
        print(f"������: {self.__format}")

my_book_1 = Book("�����", "�.�. �����������", 700)
my_book_2 = Book("1984", "������ ������", 565)
ebook_1 = EBook("������ � ���������", "������ ��������", 450, "PDF")
ebook_2 = EBook("����� � ���", "��� �������", 1225, "EPUB")

my_book_1.display_info()
my_book_2.display_info()
print("\n")
ebook_1.display_info()
ebook_2.display_info()
print("\n")
# ��� ���������
print(my_book_1.get_title())
print(ebook_1.get_title())
# � ��� �� ���������
print(my_book_1.__title)
print(ebook_1.__title)

```
![����]()
### ������
#### ������ �������� title, author, pages, � format �������� ����������, � ������ � ��� �������������� ����� ������ get_title(), get_author(), get_pages(), � get_format().

## ��������������� ������ �5
#### �������������� ���������� �����������. �� ������ ����������, �� ����, ��� ������ � ������������� ��������� (���������) � ������������ ��������. ����������� ���������� ������� ����� ������� ���� � ������������ ����� �������.

### ���������
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
        print("�����: ")
        print(f"��������: {self.__title}")
        print(f"�����: {self.__author}")
        print(f"���-�� �������: {self.__pages}")

class EBook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.__format = format

    def display_info(self):
        super().display_info()
        print(f"������: {self.__format}")

my_book_1 = Book("�����", "�.�. �����������", 700)
my_book_2 = Book("1984", "������ ������", 565)
ebook_1 = EBook("������ � ���������", "������ ��������", 450, "PDF")
ebook_2 = EBook("����� � ���", "��� �������", 1225, "EPUB")

my_book_1.display_info()
my_book_2.display_info()
print("\n")
ebook_1.display_info()
ebook_2.display_info()
print("\n")
```
![����]()
### ������
####  ����� display_info() � ������ EBook ������������� �������������� ���������� � ������� ����������� �����, ������������ ����������� � ����������� �������� ������ ������� ������������ ������ ��������� ����� ������ � ����������� �������.
