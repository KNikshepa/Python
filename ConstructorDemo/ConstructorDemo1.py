class parameterizedConstructor:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'Name is {self.name} and age is {self.age}')

obj=parameterizedConstructor('nikshu',28)
obj.display()