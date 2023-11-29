import re

def extract_words(file_path: str) -> list:
    file_handler = open(file_path, 'r', encoding='utf-8')
    text = file_handler.read()
    bunch = text.split()
    return bunch

def extract_numbers(bunch: list[str]):
    print('bunch type: [{}] bunch itself: {}'.format( type(bunch), bunch))
    text = ''.join(bunch)
    text1 = ' '.join(bunch)
    text2 = ' | '.join(bunch)

    numbers = re.findall('\d', text)

    # print(...) text1
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


# file_path = open('text.txt', 'r', encoding='utf-8')
file_path = 'text.txt'
bunch = extract_words(file_path)
extract_numbers(bunch)
'''print('Все цифры из списка: ', extract_numbers(bunch))'''