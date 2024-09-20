print ( "Hello word" )

my_list = (1,2,3,4)
for item in my_list:
    print(item)

nuber = int(input('Введите число: '))
digit_1 = nuber % 10
digit_2 = (nuber // 10) % 10
digit_3 = (nuber // 100) % 10
digit_4 = nuber // 1000
print(digit_4,digit_3,digit_2,digit_1, sep = '\n')


n1 = int(input('Введите число: '))
n2 = 0

while n1 > 0:
    digital = n1 % 10
    #print(digital)
    n1 //= 10
    print(n1)
    #n2 *= 10
    n2 += digital
print(n2)