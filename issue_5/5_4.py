def correct_estimates(arr):
    correct_arr = []
    for index, elem in enumerate(arr):

        if elem == 3:
            arr[index] = 4
        if elem != 2:
            correct_arr.append(arr[index])

    return correct_arr


one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(correct_estimates(one))
print(correct_estimates(two))
print(correct_estimates(three))
