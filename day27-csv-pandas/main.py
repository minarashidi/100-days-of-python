import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240420.csv')

#  First Solution
count_colors = data["Primary Fur Color"].value_counts()
count_colors.to_csv("squirrel_count.csv")

#  Second Solution
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Primary Fur": ["Gray", "Cinnamon", "Black"],
    "Color": [gray_count, cinnamon_count, black_count]
}

df = pd.DataFrame.from_dict(squirrel_dict)
df.to_csv("squirrel_dict_count.csv")
