# Print cubes of numbers from num1 to num2 that the user enters.
num1 = int(input('Type a number: '))
num2 = int(input('Type a number: '))
for i in range(num1, num2+1):
        print(i,'в кубе =',i**3)
