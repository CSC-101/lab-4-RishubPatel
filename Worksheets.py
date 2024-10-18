# Worksheet 1

def odd_values(n: int) -> list:
    return [13 + (2 * num) for num in range(n)]


# print(all([odd_values(4) == [13,15,17,19], odd_values(3) == [13,15,17]]))
print(odd_values(int(input("Enter an integer. "))))


def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        return 0
    return width * height


print(rectangle_area(5, 4) == 20)
print(rectangle_area(-1, 4) == 0)
print(rectangle_area(1, 0) == 0)


# Worksheet 2

class Pet(object):
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, Name: str):
        self.__name = Name

    def set_animal_type(self, Type: str):
        self.__animal_type = Type

    def set_age(self, Age: int):
        self.__age = Age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self) -> str:
        return self.__age

    def __str__(self) -> str:
        return f"Name: {self.__name}, Age: {self.__age}, Animal Type: {self.__animal_type}"


def main1():
    pet1 = Pet(input("Enter your pet's name. "), input("Enter your pet's animal type. "),
               int(input("Enter your pet's age. ")))
    print("Name:", pet1.get_name())
    print("Animal Type:", pet1.get_animal_type())
    print("Age:", pet1.get_age())


main1()


# Worksheet 3

class Car(object):
    def __init__(self, year_model: int, make: str):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self) -> float:
        return float(self.speed)


def main2():
    LightningMcQueen = Car(1983, "Chevrolet")

    for i in range(5):
        LightningMcQueen.accelerate()

    print(LightningMcQueen.get_speed())

    for i in range(5):
        LightningMcQueen.brake()

    print(LightningMcQueen.get_speed())


main2()