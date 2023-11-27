def extract_capital_words(file_path):
    capital_words = [word for word in words if word[0].isupper()]
    return capital_words


file_path = open('text.txt', 'r', encoding='utf-8')
text = file_path.read()
words = text.split()
capital_words_list = extract_capital_words(file_path)
if capital_words_list:
    for word in capital_words_list:
        print(word)
