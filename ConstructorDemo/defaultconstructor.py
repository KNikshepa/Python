class defaultConstructor:
    def __init__(self,name='user',age=23):
        self.name=name
        self.age=age

    def display(self):
        print(f'Name is {self.name} & age is {self.age}')

obj=defaultConstructor()
obj.display()
obj1=defaultConstructor('nikshu',27)
obj1.display()
