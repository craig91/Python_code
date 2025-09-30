class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
            return f"{self.name} says woof!"


fido = Dog("Fido")
print(fido.bark())

print(type(Dog))
print(type(fido))
