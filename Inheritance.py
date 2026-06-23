class Animal:
    def __init__(self,species,name):
        self.species = species
        self.name = name

class Bird(Animal):
    def __init__(self,species,name):
        super().__init__(species,name)
    
    def fly(self):
        print("The bird is flying.")

class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species, name) #pass the name and species to parent class
    def bark(self):
        print("Dog Barking!")

bird1 = Bird(species = "Pineapple Conure",name = "Zoro")
dog1 = Dog(species="Beagle",name="Tim")
flag = False
while flag != True:
    data = input("Enter the animal Dog/Bird: ").lower()
    if data == "dog":
        print(f"The name of the dog is {dog1.name} which belongs to {dog1.species} species.")
        dog1.bark()
        flag = True
    elif data == "bird":
        print(f"The name of the bird is {bird1.name} which belongs to {bird1.species} species.")
        bird1.fly()
        flag = True
    else:
        print(f"The given input {data} is invalid.")
        flag = False
        print("\nRe-Enter.....")

