import math

height_input = int(input("height of wall(m)"))
width_input = int(input("Width of wall (m)"))
coverage = 5


def paint_calc(height, width, cover):
    number_of_cans_float = (height * width) / cover
    # print(f"Not rounded number of cans {number_of_cans}")
    # rounded_number_of_cans = round("number_of_cans")  # round down
    # print(f"Rounded cans {rounded_number_of_cans}")
    number_of_cans = int(math.ceil(number_of_cans_float))  # round up
    print(f"You'll need {number_of_cans} cans of paint.")


paint_calc(height_input, width_input, coverage)
