#######

from random import randint

a = [randint(0, 30) for _ in range(randint(3, 10))]
print(a)
print([a[0]] + [a[2]] +[a[-2]])