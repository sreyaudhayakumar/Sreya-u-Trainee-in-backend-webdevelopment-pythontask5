# 3.Write a Python program to count the number of strings where the string length is 2 or more.
# 	Sample List : ['abc', 'xyz', 'aba', '1']
# 	Expected Result : 3

list_of_strings = ["a", "sreya", "jinsha", "Athira", "b"]
count = 0

for string in list_of_strings:
    if len(string) >= 2:
        count += 1
        
print("Number of strings with length 2 or more:", count)
