# "Сортировка собак"
# Создайте список объектов класса Dog. Отсортируйте этот список по возрасту (от самого молодого до самого старого).

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

    def __repr__(self):
        return f"Dog: {self.name} {self.breed} {self.age}"


dogs = [
    Dog("Lucy", "Retriever", 5),
    Dog("Lucy", "Retriever", 1),
    Dog("Lucy", "Retriever", 3),
    Dog("Lucy", "Labrador", 2),
    Dog("Lucy", "Labrador", 4),
    Dog("Lucy", "Bulldog", 1),
    Dog("Lucy", "Bulldog", 2),
    Dog("Lucy", "Bulldog", 3),
    Dog("Lucy", "Bulldog", 4),
]

dogs.sort(key=lambda dog: dog.age)

print(dogs)