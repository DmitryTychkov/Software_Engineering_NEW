'''
Магазин.
Есть списки, представляющие информацию о различных товарах в магазине.
Каждый список содержит информацию в следующем формате: (название товара, цена за единицу, количество товара).
Необходимо написать функцию, которая будет вычислять общую стоимость всех товаров в магазине.
'''
def calculate_total_cost(products):
    total_cost = 0
    for product in products:
        price_per_unit, quantity = product[1], product[2]
        total_cost += price_per_unit * quantity
    return total_cost


tests = [
    [("apple", 1.5, 10), ("banana", 2.0, 5), ("orange", 1.0, 8)],
    [("pen", 0.5, 20), ("notebook", 2.5, 10), ("pencil", 0.3, 30)],
    [("book", 10.0, 2), ("magazine", 3.0, 5), ("newspaper", 1.0, 10)]
        ]

for i, products in enumerate(tests, start=1):
    total_cost = calculate_total_cost(products)
    print(f"Тест {i}: Общая стоимость товаров в магазине: {total_cost}")