class AlternativeConstructor:
    def __init__(self,name):
        self.name=name

    @classmethod
    def from_string(cls,name_str):
        name=name_str.strip().title()
        return cls(name)
obj=AlternativeConstructor.from_string("    alice    ")
print(obj.name)