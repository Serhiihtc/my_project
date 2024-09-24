########Move an item in the list#########

list = [3, 4, 5, 6, 7, 8, 9, 12]
list.insert(0, list.pop())
print("Исходный список : " + str(list))

########will split one list into two lists############

arr = [[1, 2, 3, 4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5], [1], []]
for a in arr:
    i = len(a) - len(a) // 2
    print(a, '=>', [a[:i], a[i:]])




