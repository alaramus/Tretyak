class dom():
    def __init__(self, street, number): # описание class
        # свойства class
        self.street = street
        self.number = number
        self.age = 0


    def build(self):
        print('дом на улице', self.street, 'под номером', self.number, 'построен')

    def age_dom(self, year):
        self.age = year


dom1 = dom('сад', 120)
dom2 = dom('поле', 58)


print(dom1.street)
print((dom2.number))

dom1.build()

print(dom1.age)

dom1.age_dom(1)
print(dom1.age)