class dom():
    def __init__(self, street, number): # описание class
        # свойства class
        self.street = street
        self.number = number
        self.age = 0


class prosp(dom):
    def __init__(self, prospect, number):
        super().__init__(self, number)      # super связывает потомка с родителем!
        self.prospect = prospect


prdom = prosp('харьков', 5)
print(prdom.prospect)