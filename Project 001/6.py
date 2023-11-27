def extract_words(file_path):
    text = file_path.read()
    words = text.split()
    return words


def extract_capital_words(words):
    capital_words = [word for word in words if word[0].isupper()]
    return capital_words


file_path = open('text.txt', 'r', encoding='utf-8')
words = extract_words(file_path)
capital_words_list = extract_capital_words(words)
if capital_words_list:
    for word in capital_words_list:
        print(word)