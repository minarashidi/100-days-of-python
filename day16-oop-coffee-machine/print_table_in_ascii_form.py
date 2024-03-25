# Showcasing how to add external library and use it
from prettytable import PrettyTable

# We have a few options to put some data into our table:
# Row by row
a_table = PrettyTable()
a_table.field_names = ["Country", "City", "Population"]
a_table.add_row(["Germany", "Berlin", 3_769_495])
a_table.add_row(["Sweden", "Stockholm", 975_904])
a_table.add_row(["Norway", "Oslo", 693_494])
a_table.add_row(["Canada", "Vancouver", 675_218])
print(a_table)

# All rows at once
b_table = PrettyTable()
b_table.field_names = ["Country", "City", "Population"]
b_table.add_rows(
    [
        ["Germany", "Berlin", 3_769_495],
        ["Sweden", "Stockholm", 975_904],
        ["Norway", "Oslo", 693_494],
        ["Canada", "Vancouver", 675_218],
    ]
)
print(b_table)

# Column by column
c_table = PrettyTable()
c_table.add_column("Country", ["Germany", "Sweden", "Norway", "Canada"])
c_table.add_column("City", ["Berlin", "Stockholm", "Oslo", "Vancouver"])
c_table.add_column("Population", [3_769_495, 975_904, 693_494, 675_218])
print(c_table)
