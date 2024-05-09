def dict_pari(string):
    digit_count = {}
    for elem in string:
        if elem.isdigit():
            digit_count[int(elem)] = digit_count.get(int(elem), 0) + 1

    sorted_dict = sorted(digit_count.items(), key=lambda x: x[1], reverse=True)
    top_three = {}
    for index, (digit, count) in enumerate(sorted_dict[:3]):
        top_three[digit] = count

    return top_three

user_input = "123546234546768999923525235235233333333333333333333333333333333"
result = dict_pari(user_input)
print(result)