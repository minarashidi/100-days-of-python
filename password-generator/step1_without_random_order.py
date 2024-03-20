import random

from password_generator_data import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password += random_letter
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number
print(f"Your password is: {password}")
