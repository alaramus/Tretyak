import re

def extract_words(file_path):
    text = file_path.read()
    bunch = text.split()
    return bunch

def extract_numbers(bunch):
    numbers = re.findall('\d', ''.join(bunch))     #???
    print('Все цифры: ')
    for number in numbers:
        print(number, end=' ')                            #почему print?


'''def extract_numbers(bunch):
    store = []
    numbers = re.findall('\d', ''.join(bunch))
    for number in numbers:
       store.append(number)
    pass
    return store'''


file_path = open('text.txt', 'r', encoding='utf-8')
bunch = extract_words(file_path)
extract_numbers(bunch)
'''print('Все цифры из списка: ', extract_numbers(bunch))'''
