def find_unique_value(numbers):
    return next(number for number in numbers if numbers.count(number) == 1)

numbers = [2, 3, 5, 3, 2, 4, 5]
unique_value = find_unique_value(numbers)
print("Унікальне число:", unique_value)
