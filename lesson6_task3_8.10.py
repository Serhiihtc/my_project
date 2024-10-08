def number_multiplication(n):
    while n > 10:
        k = 1
        for i in range(len(str(n))):
            k *= int(str(n)[i])
        n = k
    print(k)

n = int(input('Enter the number: '))
number_multiplication(n)