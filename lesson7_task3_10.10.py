def second_index(text, target):
    first_index = text.find(target)
    second_index = text.find(target, first_index + 1) if first_index != -1 else -1
    return second_index if second_index != -1 else None

print(second_index("sims", "s")) 
print(second_index("find the river", "e"))
print(second_index("hello", "l"))
print(second_index("hello", "o"))