def calculate_triangle_area(a, b, c):

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

one.sort()
two.sort()
three.sort()

a_max = one[-1]
b_max =two[-1]
c_max =three[-1]

a_min = one[0]
b_min = two[0]
c_min = three[0]

s_max = calculate_triangle_area(a_max, b_max, c_max)
s_min = calculate_triangle_area(a_min, b_min, c_min)

print("Площадь треугольника из минимальных элементов, полученных из списков, равна: ", s_min)
print("Площадь треугольника из максимальных элементов, полученных из списков, равна: ", s_max)