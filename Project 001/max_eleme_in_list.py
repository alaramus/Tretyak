def GetMaxList(L):
    def is_digit(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    filtered_list = [x for x in L if is_digit(str(x))]
    if len(filtered_list) > 1:
        Max = GetMaxList(filtered_list[1:])
        if int(filtered_list[0]) < int(Max):
            return Max
        else:
            return filtered_list[0]
    if len(filtered_list) == 1:
        return filtered_list[0]


input_list = input("Введите элементы списка через запятую: ")
L = [item.strip() for item in input_list.split(',')]

num = GetMaxList(L)
print(num)
