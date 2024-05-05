from geron_4_5_2 import calculate_triangle_area

def main():
    print("Введите длины сторон треугольника:")
    try:
        a = float(input("Длина стороны a: "))
        b = float(input("Длина стороны b: "))
        c = float(input("Длина стороны c: "))

        area = calculate_triangle_area(a, b, c)
        print("Площадь треугольника:", area)
    except ValueError:
        print("Ошибка: Введены некорректные значения.")


main()