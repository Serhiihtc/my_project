import re

def clean_html(input_filename, output_filename='cleaned.txt'):
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    cleaned_content = re.sub(r'<.*?>', '', content)
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
    
    print(cleaned_content)
