########### Move all zeros to the end of the list #########

new_list = [6, 4, 0, 0, 0, 5, 8]
new_list.sort(key=bool, reverse=True)
print(new_list) 