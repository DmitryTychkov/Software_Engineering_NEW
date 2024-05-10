# Определение собственного исключения
class NegativeValueError(Exception):
    # Определение класса исключения NegativeValueError, который является подклассом встроенного класса Exception

    def __init__(self, value):
        # Метод __init__ класса NegativeValueError, который инициализирует объект исключения
        # Он принимает аргумент value, который представляет отрицательное значение
        self.value = value
        # Здесь устанавливается значение атрибута value для объекта исключения

    def __str__(self):
        # Метод __str__ класса NegativeValueError, который возвращает строку с описанием ошибки
        return f"Ошибка: значение {self.value} отрицательное."
        # Здесь формируется строка с описанием ошибки, включающая отрицательное значение

# функция, которая проверяет переданное число и выбрасывает исключение, если оно отрицательное
def process_value(value):
    # Определение функции process_value, которая принимает значение для проверки
    if value < 0:
        # Проверка, является ли значение отрицательным
        raise NegativeValueError(value)
        # Если значение отрицательное, выбрасывается исключение NegativeValueError
    else:
        print("Значение корректно.")
        # Если значение не отрицательное, выводится сообщение о корректности значения


try:
    num = int(input("Введите число: "))
    # Запрос ввода числа от пользователя и преобразование его в целое число
    process_value(num)
    # Вызов функции process_value для проверки введенного числа
except NegativeValueError as e:
    # Обработка исключения NegativeValueError
    print(e)
    # Вывод сообщения об ошибке, содержащего значение, вызвавшее ошибку

try:
    a = 10
    b = 15
    process_value(a-b)
except NegativeValueError as e:
    print(e)
