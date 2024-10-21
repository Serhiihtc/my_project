def sequence_generator(func, first_value, n):
    value = first_value
    for _ in range(n):
        yield value
        value = func(value)

def increment_by_one(x):
    return x + 1

for value in sequence_generator(increment_by_one, 0, 5):
    print(value)