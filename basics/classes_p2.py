class Dog:
    def __init__(self,name,breed,age,tired):
        self.Name = name
        self.Breed = breed
        self.Age = age
        self.Tired = tired
        print("Name: {}, Breed: {}, Age: {}".format(self.Name, self.Breed, self.Age))
    def __repr__(self):
        # __repr__ returns a representation of the object as a string
        return "Name: {}, Breed: {}, Age:{}".format(self.Name, self.Breed, self.Age)
    
    def Sleep(self):
        if self.Tired == True:
            return 'I will sleep'
        else:
            return "I don't want to sleep"
            
            
            
jack = Dog('Jack', 'Husky', 5, tired=False)
print(jack.Sleep())
print(jack.Age)
print(jack.Breed)
