# from Abstraction.AbstractionDemo import Vehicle
#
# v = Vehicle("Nikshepa", 25)
# v.display_instancemethod()
# Vehicle.display_staticemethod()
# Vehicle.display_classmethod()

from Abstraction.AbstractionDemo import Vehicle
class Bike(Vehicle):
    def __init__(self, name, age, model=None):
            super().__init__(name, age)
            self.model = model

    def abstractMethod(self):
        print(f"{self.name}'s {self.model} bike engine is now running!")

b = Bike("Nikshepa", 25, "Yamaha")
b.display_instancemethod()
b.abstractMethod()
c = Bike("Nikshepa", 26,None)
c.display_instancemethod()
c.abstractMethod()