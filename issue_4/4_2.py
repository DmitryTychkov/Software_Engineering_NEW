import random

def dice():
    result = random.randint(1, 6)
    print(result)
    if result in (5, 6):
        print('Вы победили')
    elif result in (1, 2):
        print('Вы проиграли')
    else:
        return dice()


dice()
