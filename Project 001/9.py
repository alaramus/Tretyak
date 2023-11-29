def save_text_to_file():
    file_name = "saved_text.txt"
    with open(file_name, "w", encoding='utf-8') as file:
        file.write(text)
    print('Текст сохранен в файл: ', file_name)
text = input("Enter text: ")
save_text_to_file()
print('Введеный текст: ', text)
