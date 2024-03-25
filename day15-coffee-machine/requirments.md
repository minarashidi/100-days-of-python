### Coffee Machine Program Requirements:

1. Prompt: 
    - Ask the user: “What would you like? (espresso/latte/cappuccino):”
    - Display the prompt after each action is completed.

2. Turn off the Coffee Machine:
    - Allow maintainers to turn off the machine by entering "off". 
    - Execution should end when "off" is entered.

3. Print report:
    - When the user enters “report”, display the current resource values:
        - Water: 100ml
        - Milk: 50ml
        - Coffee: 76g
        - Money: $2.5

4. Check resources:
    - Before making a drink, ensure there are enough resources available.
    - Display an error message if any resource is insufficient.

5. Process coins:
    - If resources are sufficient, prompt the user to insert coins.
    - Calculate the monetary value of the coins inserted.

6. Check transaction:
    - Verify if the user has inserted enough money for the selected drink.
    - Refund money if insufficient.
    - Add the drink cost to machine profit if transaction is successful.
    - Offer change if the user has inserted too much money.

7. Make Coffee:
    - If transaction is successful and resources are sufficient:
        - Deduct ingredients needed to make the drink.
        - Display a message: “Here is your [drink]. Enjoy!”
