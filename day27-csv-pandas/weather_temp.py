# with open('weather_data.csv') as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv
# with open('weather_data.csv') as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

# Pandas; Python data analysis library which is super powerful to perform data analysis on tabula data
import pandas as pd


def convert_temp_to_fahrenheit(temp):
    return temp * 9 / 5 + 32


data = pd.read_csv('weather_data.csv')
# temp_list = data["temp"].to_list()
# print(sum(temp_list) / len(temp_list))
print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

monday = data[data.day == "Monday"]
print(convert_temp_to_fahrenheit(monday.temp))

data_dict = {"students": ["mina", "sara", "william"],
             "scores": ["B", "A", "c"]}
new_data = pd.DataFrame(data_dict)
new_data.to_csv("students.csv")
