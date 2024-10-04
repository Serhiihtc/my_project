txt = input('Введите строку: ')

tmp = {*'''!"#$$&'()*+,-./:;<=>?@[\]^`{|}~'''}
ban = __import__('keyword').iskeyword
is_valid = True
if not txt[0].isnumeric() and not ban(txt):
    for sym in txt:
        if sym.isupper() or sym in tmp:
            is_valid = False
            break
else:
    is_valid = False

print(is_valid)            