def difference(*args):
    return round(max(args) - min(args), 2) if args else 0

print(difference(1, 2, 3))         
print(difference(-1.5, 2.3))       
print(difference())                
print(difference(9.999, -9.999))   
