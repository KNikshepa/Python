from abc import ABC, abstractmethod

global_var='I am global var'
_privateglobalvar='I am private global var'

class Vehicle(ABC):
    class_var='I am class variable'
    __private_classvar='I am are private class variable'

    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def display_instancemethod(self):
        print(_privateglobalvar)
        print(Vehicle.__private_classvar)
        print(self.name)
        print(self.__age)

    @staticmethod
    def display_staticemethod():
        print(_privateglobalvar)
        print(Vehicle.__private_classvar)
        # print(self.name)
        # print(self.__age)

    @classmethod
    def display_classmethod(cls):
        print(_privateglobalvar)
        print(cls.__private_classvar)
        # print(self.name)
        # print(self.__age)

    @abstractmethod
    def abstractMethod(self):
        pass

# v = Vehicle("Nikshepa", 25) this gives an error
# v.display_instancemethod()
# Vehicle.display_staticemethod()
# Vehicle.display_classmethod()