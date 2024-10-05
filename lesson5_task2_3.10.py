while True:
    x = float(input())
    y = input()
    z = float(input())

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
    if s == 'y' or s == 'Yes':
        break
    else:
        print('Тогда считаем дальше.')