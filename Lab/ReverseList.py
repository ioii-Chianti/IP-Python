def reverse_list(element):
    if type(element) == list:
        newList = []
        for data in element:
            newList.insert(0, reverse_list(data))
        return newList
    else:
        return element

print(eval(input())) # MUST add this line.
# print(reverse_list([1, 2, [3, 4, [5, 6]], 7]))