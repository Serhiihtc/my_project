####Calc####

print("Для завершения операции введите 0 в качестве знака операции")

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
            print("Деление на ноль!")

########Move an item in the list#########
list = [3, 4, 5, 6, 7, 8, 9, 12]
list.insert(0, list.pop())
print("Исходный список : " + str(list))


########

lst = ['cow', 1, 'cat', 2, 'dog', 3]
animals = []
num = []
for i in list:
    num.append(i) if i.isnumeric() else animals.append(i)
    
