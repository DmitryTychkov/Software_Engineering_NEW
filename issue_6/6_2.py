import pprint


def remove_first_occurrence(tup, element):

    if element not in tup:
        return tup

    index = tup.index(element)
    new_tup = tup[:index] + tup[index+1:]

    return new_tup


tests = [((1, 2, 3), 1),
         ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
         ((2, 4, 6, 6, 4, 2), 9)]

for test in tests:

    result = remove_first_occurrence(test[0], test[1])
    print(result)