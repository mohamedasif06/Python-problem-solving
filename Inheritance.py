class Animal:
    def __init__(self,name):
        self.name = name
        self.is_pet = True

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name) #pass the name to parent class
        self.breed = breed
    
    def describe(self):
        print(f"The {self.name} is a {self.breed}.")

dog1 = Dog(name = "Jimmy",breed = "Labrodor")
dog2 = Dog(name = "Tim",breed = "Doberman")
dog1.describe()
dog2.describe()

