weather_in_celsius = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

# (temp_c * 9/5) + 32 = temp_f
weather_in_fahrenheit = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_in_celsius.items()}
print(weather_in_fahrenheit)
