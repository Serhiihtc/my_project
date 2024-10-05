while True:
    x = float(input("1st num: "))
    y = input("operator: ")
    z = float(input("2 nd num: "))

    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/' and z == 0:
        print("Делитель не равен 0")
    elif y == '/':
        print(x / z)

    s = input('Считаем дальше? ')
    if s == 'y' or s == 'yes':
        break
    else:
        print('Тогда считаем дальше.')