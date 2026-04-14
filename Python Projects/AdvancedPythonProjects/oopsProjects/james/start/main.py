class Person:
    ...


john = Person()
john.name = "Kon"
john.age = 50
# print(dir(john))
# print(john.name, john.age)

class Person:
    def __init__(self, name, age) -> None:
        self.name = name.title()
        self.age = age +2


john= Person("jhon", 45)
print(john.name, john.age)
#  vars returns allatributes of an instane in a dictionary 
print(vars(john))