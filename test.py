print ( "Hello word" )

my_list = (1,2,3,4,5)
for item in my_list:
    print(item)

n = int(input('Введите число: '))
while n > 0:
    last = n % 2
    print(last)
    n = n // 2



n1 = int(input('Введите число: '))
n2 = 0

while n1 > 0:
    digital = n1 % 10
    print(digital)
    n1 //= 10
    print(n1)
    n2 *= 10
    n2 += digital
print(n2)