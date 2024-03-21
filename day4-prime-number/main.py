# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

input_number = int(input("Enter a number: "))


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


prime_checker(input_number)
