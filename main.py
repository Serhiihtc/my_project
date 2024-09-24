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

