import calendar
def cal(y, m):
    return(calendar.month(yy, mm))     # NO PRINT!!!


yy = int(input('year: '))
mm = int(input('month: '))
print(cal(yy, mm))