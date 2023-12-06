
def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line


with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for result in grep(lines, 'важно'):
        print(result)
