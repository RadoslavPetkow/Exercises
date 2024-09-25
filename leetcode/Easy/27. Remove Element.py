my_list = [1, 2, 3, 3, 4, 3, 5]
x = 3
my_list = [element for element in my_list if element != x]
print(my_list)  # Output: [1, 2, 4, 5]