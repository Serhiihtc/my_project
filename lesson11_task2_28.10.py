def generate_cube_numbers(limit):
    num = 2
    while (cube := num ** 3) < limit:
        yield cube
        num += 1

for cube in generate_cube_numbers(1000):
    print(cube)
