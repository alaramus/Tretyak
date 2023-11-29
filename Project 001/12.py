import re
def extract_words(file_path: str) -> list:
    file_handler = open(file_path, 'r', encoding='utf-8')
    text = file_handler.read()
    bunch = text.split()
    return bunch

def extract_numbers(bunch: list[str]):
#    numbers = re.findall(r'\b\d+\b', ' '.join(bunch))            регуляр - шаблон поиска подстрок в тексте
    store = []
    for item in bunch:
        if item.replace('.', '').isdigit():  #проверяет, состоит ли строка только из цифр. не будут распознаны как цифры, если в них есть точка, минус
            store.append(item)
    return store

def extract_numbers_minus(bunch: list[str]):
    store_minus = []
    for item in bunch:
        if item.replace('-', '').isdigit():
            store_minus.append(item)
    return store_minus

def extract_six_letters(bunch: list[str]):
    six_letters = set()               # множество хранит только уникальные элементы
    for item in bunch:
        item = item.replace('.', '')
        item = item.replace(',', '')
        if len(item) == 6:
            six_letters.add(item)               # add = append для множеств
    return list(six_letters)

file_path = 'text.txt'
bunch = extract_words(file_path)
print('Весь текст из файла: ', extract_words(file_path))
print('Все цифры из списка: ', extract_numbers(bunch), extract_numbers_minus(bunch))
print('Все слова с 6 буквами: ', extract_six_letters(bunch))

