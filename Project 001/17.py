import re

def find_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        numbers = re.findall(r'-?\d+(?:\.\d+)?', content)
    return numbers


file_path = 'text.txt'
found_numbers = find_numbers(file_path)

print("Найденные числа в файле:", found_numbers)

# '-'?: cимвол - указывает на возможное!!! наличие минуса перед числом. ? делает предыдущий символ необязательным

# \d+: \d представляет любую цифру от 0 до 9, а + указывает на то, что цифра может встречаться один или более раз

# (?:\.\d+)?: десятичная часть числа

# (?: ... ): используется для группировки выражения
# \.:  символ точки
# ?:  знак ? в конце  указывает, что предыдущая группа необязательна

# *