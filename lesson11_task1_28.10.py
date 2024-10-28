def prime_generator(limit):
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num

print(list(prime_generator(10)))
