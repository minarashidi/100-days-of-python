"""
The goal of this game is to stay alive as long as possible and score as high as possible by thinking about who might be
more popular than the other.
"""

from art import logo
from art import vs
from game_data import data
import random
import os


def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def check_answer(guess, first_account, second_account):
    if first_account['follower_count'] > second_account['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    should_continue = True
    while should_continue:
        first_random = random.choice(data)
        print(f"Compare A: {first_random['name']}, {first_random['description']}, from {first_random['country']}")

        print(vs)

        second_random = random.choice(data)
        print(f"Compare B: {second_random['name']}, {second_random['description']}, from {second_random['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, first_random, second_random)
        clear()
        print(logo)
        if is_correct:
            score += 1
            print("You are correct! current score: " + str(score))
        else:
            print("Sorry, that's wrong. Final score: " + str(score))
            should_continue = False


game()
