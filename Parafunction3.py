def calculate_average(*numbers):
    if len(numbers) == 0:
        print("Please provide at least one number.")
        return
    return sum(numbers) / len(numbers)

average = calculate_average(1, 2, 3, 4, 5)
print(average)

calculate_average()