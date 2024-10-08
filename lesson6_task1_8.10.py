from string import ascii_letters

a, b = input()

print(ascii_letters[ascii_letters.index(a):ascii_letters.index(b) + 1])