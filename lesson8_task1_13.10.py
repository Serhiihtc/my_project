def add_one(digits):
    return [int(digit) for digit in str(int(''.join(map(str, digits))) + 1)]

digits = [1, 2, 3, 4]
new_digits = add_one(digits)
print(new_digits)