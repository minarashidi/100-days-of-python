MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def report_current_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def get_coins():
    print("Please insert coins")
    total = int(input("How many quarters would you like to pay?")) * 0.25
    total += int(input("How many dimes would you like to pay?")) * 0.10
    total += int(input("How many nickles would you like to pay?")) * 0.05
    total += int(input("How many pennies would you like to pay?")) * 0.01
    return total


def is_payment_successful(received_money, cost):
    if received_money >= cost:
        remaining = round(received_money - cost, 2)
        print(f"Here is: {remaining} in change")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, you haven't inserted enough money. Money refunded.")
        return False


def make_coffee(name, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {name}. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso, latte or cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == "report":
        report_current_resources()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = get_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
