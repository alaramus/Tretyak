import re
def extract_words(file_path):
    text = file_path.read()
    bunch = text.split()
    return bunch

def extract_numbers(bunch):
    numbers = re.findall('\d', ''.join(bunch))
    print('Все цифры: ')
    for number in numbers:
        print(number)     # end=' '

def extract_capital_words(bunch):
    capital_words = [word for word in bunch if word[0].isupper()]
    print('Все слова с большой буквы: ')
    print(capital_words)

def exrtact_lowercase_letters(bunch):
    lowercase_letters = [word for word in bunch if word[0].islower()]
    print('Все слова с маленькой буквы: ')
    print(lowercase_letters)


file_path = open('text.txt', 'r', encoding='utf-8')
bunch = extract_words(file_path)
extract_numbers(bunch)
extract_capital_words(bunch)
exrtact_lowercase_letters(bunch)
