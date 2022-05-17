# class Animal:
#     name: str
#
#     def __init__(self, name):
#         self.name = name
#
#     def says(self):
#         return self
#
#
# class Cat(Animal):
#
#     def says(self):
#         return f"{self.name} - a cat. It says MEOW."
#
#
# class Dog(Animal):
#
#     def says(self):
#         return f"{self.name} - a dog. It says WOOF."
#
#
# class Cow(Animal):
#
#     def says(self):
#         return f"{self.name} - a cow. It says MUU."
#
#
# cat_1 = Cat("Sindy")
# dog_1 = Dog("Sparky")
# cow_1 = Cow("Dosya")
#
# print(cat_1.says())
# print(dog_1.says())
# print(cow_1.says())


# _______________________________________
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_perimeter(self):
        return self

    @abstractmethod
    def get_square(self):
        return self


class Circle(Shape):
    r: float

    def __init__(self, r):
        self.radius = r

    def get_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

    def get_square(self):
        square = 3.14 * self.radius ** 2
        return square


class Rectangle(Shape):
    a: float
    b: float

    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def get_perimeter(self):
        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

    def get_square(self):
        square = self.side_a * self.side_b
        return square


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)


a = Circle(3)
b = Rectangle(2, 2)
c = Square(5)
print(a.get_perimeter())
print(a.get_square())
print(b.get_perimeter())
print(b.get_square())
print(c.get_perimeter())
print(c.get_square())
