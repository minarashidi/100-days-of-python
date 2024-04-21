# List Comprehension
numbers = [1, 2, 3, 4, 5]
new_list = [n + 1 for n in numbers]
print(new_list)

# String as List
firstname = "MINA"
new_name = [char + char for char in firstname]

# Range as List
range_list = [n * 2 for n in range(2, 5)]

# Conditional List Comprehension
names = ["Alex", "Nick", "Bob", "Charlie", "William"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# Square Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)

# Filter out Even Numbers
list_of_string = input("Enter a string: ").split(",")
list_of_integer = [int(n) for n in list_of_string]
even_numbers = [n for n in list_of_integer if n % 2 == 0]
print(even_numbers)

