# 7. Write a Python program to find the repeated items of a tuple.

def find_repeated_items(input_tuple):
    repeated_items = []
    for item in input_tuple:
        if input_tuple.count(item) == 2 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

input_tuple = (1, 2, 2, 3, 3, 4, 5, 6, 6)
repeated = find_repeated_items(input_tuple)
print("orginal tuple is:",input_tuple)
print("Repeated items from tuple:", repeated)


