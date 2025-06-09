class Bike:
    def __init__(self, name, age, model=None):
        self.name = name
        self.age = age
        self.model = model

    @classmethod
    def from_basic(cls, name, age):
        return cls(name, age)  # model will be None

    @classmethod
    def from_full_details(cls, name, age, model):
        return cls(name, age, model)

b1 = Bike.from_basic("Nikshepa", 25)             # uses model=None by default
b2 = Bike.from_full_details("Nikshepa", 25, "Yamaha")  # provides all details


