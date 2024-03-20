import random

from password_generator_data import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password_list.append(random_letter)
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)
for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password_list.append(random_number)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
