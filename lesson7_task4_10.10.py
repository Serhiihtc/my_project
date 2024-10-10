def common_elements():
    return {x for x in range(100) if x % 3 == 0} & {x for x in range(100) if x % 5 == 0}

result = common_elements()
print(result)
