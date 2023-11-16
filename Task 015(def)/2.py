# sums all integers from the value "start" to the value "end" inclusive
a= int(input('Введити первое число'))
b= int(input('Введити второе число'))
def sum_range(start, end):
    if start > end:                    # Если False то дальше не выполняется?
        end, start = start, end
    return sum(range(start, end + 1))


print(sum_range(a, b))
