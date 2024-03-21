country = input("Add country name\n")
visits = int(input("Number of visits\n"))
list_of_cities = eval(input("List of visited cities\n"))

travel_log = [
    {
        "country": "Italy",
        "visits": 4,
        "cities": ["Rome", "Milan", "Florance"]
    },
    {
        "country": "Germany",
        "visits": 6,
        "cities": ["Berlin", "Munich", "Frankfurt"]
    },
]


def add_new_country(name, times_visited, cities_visited):
    new_country = {"country": name, "visits": times_visited, "cities": cities_visited}
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
