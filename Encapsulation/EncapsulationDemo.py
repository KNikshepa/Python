class Person:
    __class_var='I am class variable'

    def __init__(self,name,age):
        self.name=name
        self.__age=age

    #Getter method
    def get_age(self):
        return self.__age

    #Setter method
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print('Age must be positive')

    def display(self):
        print('Name is ',self.name)
        print('Age is ',self.__age)

obj=Person('nikshu',28)
obj.display()
obj.set_age(20)
print(obj.get_age())
obj.name='shshsh'
#obj.__age cannot be modified need to use set for it