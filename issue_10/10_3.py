def calculate_with_except():
    try:
        number = int(input("Введите число: "))
        result = 2 + number
        print("Результат сложения:", result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


print("Тест 1: ввод числа")
calculate_with_except()

print("\nТест 2: ввод строки")
calculate_with_except()

print("\nТест 3: ввод другого неподходящего типа данных")
calculate_with_except()
