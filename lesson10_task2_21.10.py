def first_word(text: str) -> str:
    words = text.replace(',', ' ').replace('.', ' ').split()
    return words[0] if words else ""

print(first_word("Hello, world!"))
print(first_word("...and then."))
print(first_word("Привіт, як справи?"))
print(first_word("   'word"))