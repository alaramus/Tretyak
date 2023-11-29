import re

def extract_words(file_path: str) -> list:
    file_handler = open(file_path, 'r', encoding='utf-8')
    text = file_handler.read()
    bunch = text.split()
    return bunch

def extract_numbers(bunch: list[str]):
    print('bunch type: [{}] bunch itself: {}'.format(type(bunch), bunch))
    text = ''.join(bunch)                       # join отвечает за объединение списка строк с помощью определенного указателя
    text1 = ' '.join(bunch)
    text2 = ' | '.join(bunch)

    print('text type: {} text itself: "{}"'.format(type(text), text))
    print('text type: {} text itself: {}'.format(type(text1), text1))
    print('text type: {} text itself: {}'.format(type(text2), text2))
    '''numbers = re.findall('\d', ' '.join(bunch))'''             #регуляр шаблон поиска подстрок в тексте
    store = []
    for item in bunch:
        if item.isdigit():                     # Выбирает только цифры выделеные пробелом с двух сторон ?
            store.append(item)
    return store

file_path = 'text.txt'
bunch = extract_words(file_path)

print('Все цифры из списка: ', extract_numbers(bunch))
