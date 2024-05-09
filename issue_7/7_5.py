'''у нас есть текстовый файл 7_5.txt, в котором записан список покупок каждого дня.
Каждая строка представляет собой один день и содержит список продуктов, которые были куплены в этот день.
Требуется написать программу, которая считывает этот файл и выводит в терминал общее количество покупок за каждый день.
'''


def load_shopping_list(file_name):
    shopping_list = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            date, items = line.strip().split(': ')
            shopping_list[date] = items.split(', ')
    return shopping_list

def total_items_per_day(shopping_list):
    total_items = {}
    for date, items in shopping_list.items():
        total_items[date] = len(items)
    return total_items

def main():
    file_name = "text/7_5.txt"
    shopping_list = load_shopping_list(file_name)
    print("Общее количество покупок за каждый день:")
    for date, total_items in total_items_per_day(shopping_list).items():
        print(f"{date}: {total_items}")


main()