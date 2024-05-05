# импорт класса datetime из модуля datetime
from datetime import datetime
# импорт класса sqrt из модуля math
from math import sqrt

def main(**kwargs):
    """
    Определили функцию main
    :param kwargs: в аргументы вкладывается словарь
    Каждый элемент представляет пару ключ -> значение
    :return:
    """
    for key in kwargs.items():
        # Вычисление длины гипотенузы прямоугольного треугольника
        result = sqrt(key[1][0] ** 2 + key [1][1] ** 2)
        # Вывод результата в консоль
        print(result)
# Проверка, что программа запущена напрямую
if __name__ == '__main__':
    # запись текущего времени перед выполнением программы
    start_time = datetime.now()
    # Вызов функции main с передачей аргументов
    main(
        one=[10,3],
        two=[5,4],
        three=[15,13],
        four=[93,53],
        five=[133, 15]
    )
    # Вычисление времени выполнения программы
    time_costs = datetime.now() - start_time
    # Вывод времени выполнения программы
    print(f"Время выполнения программы - {time_costs}")