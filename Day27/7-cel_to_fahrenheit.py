# converting celsius to fahrenheit of a wek data from a dictionary

weather_c={
    'Monday': 12,
    'Tuesday':14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}

# tempc * 9/5 + 32

weather_f={day:((tempc*9/5)+32) for (day,tempc) in weather_c.items() }
print(weather_f)