stack = []
for i in range(1, 11):
    stack.append(f'{i}-й элемент')
    print(f'+ {i}-й элемент добавлен')
    for i in stack:
        print(i, end=" ")
print('\n')
for i in range(len(stack)):
    print('В стеке: ', end=" ")
    for i in stack:
        print(i, end=" ")
    print(f'\n{stack.pop()} удален из стека')