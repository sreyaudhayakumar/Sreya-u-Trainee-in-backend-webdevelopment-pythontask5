# Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
# list1=[2, 4, 6, 8, 10, 12, 14]

list1 = [2, 4, 6, 8, 10, 12, 14]

print("Original list:", list1)

for i in list1:
    square = i ** 2
    if square > 50:
        print("Square of", i, "is greater than 50:", square)
