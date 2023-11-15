# read text from t.txt
f = open('t.txt')
line = f.readline()
while line:
    print(line,end = '')
    line = f.readline()
f.close()