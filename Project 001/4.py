def extract_capital_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            capital_words = [word for word in words if word[0].isupper()]
            return capital_words
    except FileNotFoundError:
        return


file_path = 'text.txt'
capital_words_list = extract_capital_words(file_path)
if capital_words_list:
    for word in capital_words_list:
        print(word)
