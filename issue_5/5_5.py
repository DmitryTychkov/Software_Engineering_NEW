list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def generate_sets(input_list):
    # —оздаем словарь дл€ подсчета повторений чисел
    count_dict = {}
    for num in input_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    result_set = set()
    # ‘ормируем множество с учетом повторений чисел
    for num, count in count_dict.items():
        result_set.add(num)
        for i in range(2, count + 1):
            result_set.add(str(num) * i)

    return result_set

print(generate_sets(list_1))
print(generate_sets(list_2))
print(generate_sets(list_3))