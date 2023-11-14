# Selection for medical examination. For ages 20-25, 35-40, 55-60. Send the rest home
age = int(input("Enter your age: "))
if age >= 20 and age <= 25:
    name1 = input("Enter your first name")
    name2 = input("Enter your last name")
elif age >= 35 and age <= 40:
    name1 = input("Enter your first name")
    name2 = input("Enter your last name")
elif age >= 55 and age <= 60:
    name1 = input("Enter your first name")
    name2 = input("Enter your last name")
else:
    print("People of your age today are not examined")
