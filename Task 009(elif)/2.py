# chat bot с командами : help, joke, fairy tale, news, task list, creating a note, new contact
comand = input('Введите требуемое действие(для вызова справки введите help): ')
if comand == 'help':
    print('Доступные команды: joke, fairy tale, news, task list, creating a note, new contact')
elif comand == 'joke':
    print('Ха-ХА')
elif comand == 'fairy tale':
    print('land far far away')
elif comand == 'news':
    print('Everything will be fine')
elif comand == 'task list':
    print('1.Wake up')
    print('2.Eat')
    print('3.Sleep')
elif comand == 'creating a note':
    note = input('введите текст: ')
elif comand == 'new contact':
    name1 = input("write down first name: ")
    name2 = input("write down last name: ")
    tel = int(input("write down mobile number: "))
else:
    print('unsupported command')


