####Calc####
#print("Для завершения операции введите 0")

while True:
    a = float(input('Введите первое число '))
    b = float(input('Введите второе число '))
    s =input("Знак (+, -, *, /,): ")
    if s == '0':
        break
    if s not in ('+', '-', '*', '/'):
        continue

    if s == '+':
        print(a + b)
    elif s == '-':
        print(a - b)
    elif s == '*':
        print(a * b)
    elif s == '/':
        if b != 0:
            print(a * b)
        else:
            print("Деление на ноль !")
    

