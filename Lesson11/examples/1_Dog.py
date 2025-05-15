class Dog:
    species = "Canis familiaris"
    paws = 4

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_hungry = True

    def bark(self):
        print(f"{self.name} says Woof! Woof!")

    def eat(self, food):
        if self.is_hungry:
            print(f"{self.name} is happily eating {food}.")
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry right now.")