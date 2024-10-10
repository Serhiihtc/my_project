def correct_sentence(string):
    if not string:
        return ""
    
    string = string[0].upper() + string[1:]
    if string[-1] != ".":
        string += "."
    
    return string

input_string = input("Enter a sentence: ")
corrected = correct_sentence(input_string)
print("Corrected sentence:", corrected)