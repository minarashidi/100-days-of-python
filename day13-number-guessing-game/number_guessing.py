from art import logo
import random

EASY_DIFFICULTY_LEVEL = 10
HARD_DIFFICULTY_LEVEL = 5


def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty_level == "easy":
        return EASY_DIFFICULTY_LEVEL
    else:
        return HARD_DIFFICULTY_LEVEL


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    random_number = random.randint(1, 100)
    total_attempts = set_difficulty()

    attempts = 0
    while attempts < total_attempts:
        print(f"You have {total_attempts - attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        attempts += 1
        if guess == random_number:
            print("You guessed correctly!")
            return
        elif guess < random_number:
            print("Your guess is too low")
        elif guess > random_number:
            print("Your guess is too high")

    # Check if the user has run out of attempts
    if attempts == total_attempts:
        print("Game over! You've run out of attempts.")
        print(f"The correct number was {random_number}.")


game()
