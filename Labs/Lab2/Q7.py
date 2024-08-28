
temperatures = [72, 75, 78, 77, 80, 85, 90, 88, 83, 82, 79, 76, 74, 71, 70, 73, 77, 79, 82, 86, 88, 91, 92, 89, 87, 84, 81, 78, 75, 73]


def calculate_average(temp_list):
    avg_temp = sum(temp_list) / len(temp_list)
    print(f"Average temperature for the month: {avg_temp:.2f}°F")

def find_high_low(temp_list):
    highest_temp = max(temp_list)
    lowest_temp = min(temp_list)
    print(f"Highest temperature: {highest_temp}°F")
    print(f"Lowest temperature: {lowest_temp}°F")


def sort_temperatures(temp_list):
    sorted_temps = sorted(temp_list)
    print(f"Temperatures in ascending order: {sorted_temps}")


def remove_temperature(temp_list, day_index):
    if 0 <= day_index < len(temp_list):
        removed_temp = temp_list.pop(day_index)
        print(f"Removed temperature for day {day_index + 1}: {removed_temp}°F")
    else:
        print("Invalid day index.")


calculate_average(temperatures)
find_high_low(temperatures)
sort_temperatures(temperatures)


day_to_remove = 9  # Note: Days are 1-based, list indices are 0-based
remove_temperature(temperatures, day_to_remove)


print(f"Updated temperature list: {temperatures}")
