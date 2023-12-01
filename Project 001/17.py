import re

def find_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        numbers = re.findall(r'-?\d+(?:\.\d+)?', content)
    return numbers


file_path = 'text.txt'
found_numbers = find_numbers(file_path)

print("Найденные числа в файле:", found_numbers)

