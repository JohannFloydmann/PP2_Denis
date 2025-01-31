def unDuplicate(first):
    second = list()
    for el in first:
        if second.count(el) == 0:
            second.append(el)
    return second

print(unDuplicate([1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 6]))