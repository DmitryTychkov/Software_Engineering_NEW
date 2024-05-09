def employee(typ, element):
    if element not in typ:
        return ()

    first_index = typ.index(element)
    last_index = typ.index(element, first_index + 1) if typ.count(element) > 1 else len(typ)

    return typ[first_index:last_index + 1]


tests = [((1, 2, 3), 8),
         ((1, 8, 3, 4, 8, 8, 9, 2), 8),
         ((1, 2, 8, 5, 1, 2, 9), 8)]

for typ, element in tests:
    result = employee(typ, element)
    print(result)