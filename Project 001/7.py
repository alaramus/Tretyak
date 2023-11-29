def extract_words(file_path):
    text = file_path.read()
    bunch = text.split()
    return bunch



def extract_numbers(bunch):
    store = []
    for item in bunch:
        if item.isdigit():   # Выбирает только цифры выделеные пробелом с двух сторон ?
            store.append(item)
    return store


file_path = open('text.txt', 'r', encoding='utf-8')
bunch = extract_words(file_path)

print('Все цифры из списка: ', extract_numbers(bunch))
