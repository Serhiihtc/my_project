print ( "Hello word" )

my_list = (1,2,3,4,5)
for item in my_list:
    print(item)



n = input('введите число')
printChar(n) 
def ShowCif(a):
    if a>0:
        ShowCif(a/10)
        print(a%10)

ShowCif(1234)


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