def mid_value(*args):
    if len(args) == 0:
        return None
    sum_value = sum(args)
    sr_value = sum_value / len(args)
    return sr_value


values = input('Введите значения через пробел: ')
numbers = [int(num.strip()) for num in values.split(' ')]
print(mid_value(*numbers))
