# 4.Write a Python program to print the numbers of a specified listafter removing even numbers from it
# 	list = [24,34,53,65,78,93,23,42]

list = [24, 34, 53, 65, 78, 93, 23, 42]
odd_list = []

for number in list:
    if number % 2 != 0:
        odd_list.append(number)
        
print("orginal list",list)
print("Numbers after removing even numbers:", odd_list)
