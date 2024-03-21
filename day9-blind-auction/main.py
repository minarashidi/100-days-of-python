import os
from art import logo


def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)
bids = {}


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")


continue_bidding = True
while continue_bidding:
    name = input("What is your name?")
    bid = int(input("What is your bid? : $"))
    bids[name] = bid
    other_bidders = str(input("Are there any other bidders? Type 'yes' or 'no'"))
    if other_bidders == "yes":
        clear()
    elif other_bidders == "no":
        continue_bidding = False
        find_highest_bid(bids)
