def fibonacci_gen():

    a, b = 1, 1

    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_gen()

# Записываем все числа Фибоначчи в файл
with open("text/11_2.txt", "w") as file:
    for _ in range(200):
        fib_number = next(fib_gen)
        file.write(str(fib_number) + "\n")

# Получаем последнее число Фибоначчи
last_fib_number = fib_number

print("Последнее число Фибоначчи:", last_fib_number)

