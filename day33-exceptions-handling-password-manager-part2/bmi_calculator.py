height = float(input("Enter your height in meter: "))
weight = int(input("Enter your weight in kg: "))
if height > 3:
    raise ValueError(f"Height shouldn't be greater than {height}")
bmi = weight / (height ** 2)
print(f"Your bmi is {bmi}")
