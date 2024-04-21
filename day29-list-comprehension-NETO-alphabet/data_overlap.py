# Create a list which contains the numbers that are common in both file1 and file2.
with open("file1.txt") as file1:
    list_one = file1.readlines()

with open("file2.txt") as file2:
    list_two = file2.readlines()
result = [int(num) for num in list_one if num in list_two]

print(result)
