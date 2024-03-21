# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
number_of_people = int(input("How many people to split the bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
total_bill_with_tip = (bill * tip / 100) + bill
bill_per_person = total_bill_with_tip / number_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay $ {final_amount}")
