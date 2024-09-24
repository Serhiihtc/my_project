####Calc####
a = float(input('Введите первое число '))
b = float(input('Введите второе число '))
action =input('Введите действие (+ - / *): ')

if action == '+':
    print(a + b)
elif action == '-':
    print(a - b)
elif action == '/':
    print(a / b)
elif action == '*':
    print(a * b)
else:
    print('Вы вели неверное действие')
    

