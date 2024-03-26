class Animal:
    def __init__(self, name, species):  # Constructor for the Animal class
        self.name = name  # Assigning the name attribute
        self.species = species  # Assigning the species attribute

    def make_sound(self):  # Method to make a sound
        print("Sounds made by the animal")

class Dog(Animal):  # Dog class inheriting from Animal class
    def __init__(self, name, breed):  # Constructor for the Dog class
        Animal.__init__(self, name, species="Dog")  # Calling the constructor of the parent class
        self.breed = breed  # Assigning the breed attribute

    def make_sound(self):  # Method to make a sound, overrides the method in the parent class
        print("Bark")

# Creating an instance of the Dog class
d = Dog("Buddy", "Golden Retriever")
# Calling the make_sound method of the Dog class
d.make_sound()

# Creating an instance of the Animal class
a = Animal("Leo", "Lion")
# Calling the make_sound method of the Animal class
a.make_sound()
