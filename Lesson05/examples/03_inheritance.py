# Родительский класс
class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return f"{self.name} {self.surname}"


# Дочерний класс
class Student(People):
    def __init__(self, name, surname, university, payment):
        People.__init__(self, name, surname)
        # Добавляем уникальные атрибуты
        self.learning_university = university
        self.__money = 1000 # _Student__money
        self.__payment = payment

    def pay_education(self):
        self.__money -= self.__payment


# Дочерний класс
class Teacher(People):
    def __init__(self, name, surname, university, salary):
        People.__init__(self, name, surname)
        # Добавляем уникальные атрибуты
        self.teaching_university = university
        self.__money = 1000
        self.__salary = salary

    # Уникальный метод Учителя
    def get_salary(self):
        self.__money += self.__salary


student = Student("Альберт", "Эдуардович", "Технический университет", 150)
print(student.get_full_name())
# teacher = Teacher("Альберт", "Эдуардович", "Технический университет", 2000)
# print(teacher.name)
# print(teacher.teaching_university)
