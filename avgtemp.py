import numpy as np

def analyze_temperature(temperatures):
    temps_array = np.array(temperatures)

    # Calculate average, maximum, and minimum temperatures
    avg_temp = np.mean(temps_array)
    max_temp = np.max(temps_array)
    min_temp = np.min(temps_array)

    return avg_temp, max_temp, min_temp

# Insert temperatures for the upcoming week
weekly_temperatures = [55, 55.6, 63, 68.2, 56.3, 54, 48]

average_temp, maximum_temp, minimum_temp = analyze_temperature(weekly_temperatures)

print(f"Average temperature for the week: {average_temp}°F")
print(f"Maximum temperature for the week: {maximum_temp}°F")
print(f"Minimum temperature for the week: {minimum_temp}°F")
if average_temp > 65:
    print("It's a warm week!")
else:
    print("It's a cooler week.")
