# Добавьте в класс Dog новый метод get_age_category(), который будет возвращать строку,
# определяющую возрастную категорию собаки на основе ее атрибута age. Например:

# 0-1 год: "Puppy"
# 1-7 лет: "Adult"
# Старше 7 лет: "Senior"
# Затем создайте несколько объектов Dog с разным возрастом и выведите их имя и возрастную категорию, используя новый метод.

# Примечание: исходный класс Dog, можно взять в examples

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

    def get_age_category(self):
        # 0-1 год: "Puppy"
        # 1-7 лет: "Adult"
        # Старше 7 лет: "Senior"
        if self.age <= 1:
            return "Puppy"
        elif 2 <= self.age <= 7:
            return "Adult"
        else:
            return "Senior"