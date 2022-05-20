class Car:

    def __init__(self, brand, model, issue_year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__issue_year = issue_year
        self.__speed = speed

    def speed_increase(self):
        self.__speed += 5
        return self.__speed

    def speed_decrease(self):
        self.__speed -= 5
        return self.__speed

    def stop(self):
        self.__speed = 0
        return self.__speed

    def speed_actual(self):
        print(self.__speed)

    def reversal(self):
        self.__speed = -self.__speed
        return self.__speed


mercedes = Car("Mercedes", "C300", 2019, 20)
mercedes.reversal()
mercedes.speed_increase()
mercedes.speed_actual()
mercedes.speed_increase()
mercedes.reversal()
mercedes.speed_actual()
mercedes.speed_increase()
print(mercedes._Car__speed)


#___________________________________________________________________________

class Dog:

    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    @property
    def species(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def age(self):
        return self.__age

    @species.setter
    def species(self, new_species):
        self.__name = new_species

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def voice(self):
        print(f"And it barks: I can be your friend!")

    def display_info(self):
        print(f"The Dog nicknamed {self.__name} has {self.__color} fur and is {self.__age} years old.")
        Dog.voice(self)

dog = Dog("Sparky", "brown", 8)
dog.display_info()


class Phone:

    def __init__(self, brand, model, color):
        self.__brand = brand
        self.__color = color
        self.__model = model

    @property
    def brand(self):
        return self.__brand

    @property
    def color(self):
        return self.__color

    @property
    def model(self):
        return self.__model

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    def performance(self):
        print(f"It's is an average level.")

    def display_info(self):
        print(f"This phone {self.__brand} {self.__model} is {self.__color}.")
        Phone.performance(self)

phone = Phone("Motorola", "Razor", "pink")
phone.display_info()


class Home:

    def __init__(self, area, color, floor):
        self.__area = area
        self.__color = color
        self.__floor = floor

    @property
    def area(self):
        return self.__area

    @property
    def color(self):
        return self.__color

    @property
    def floor(self):
        return self.__floor

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @floor.setter
    def floor(self, new_floor):
        self.__floor = new_floor

    def trees(self):
        number_of_trees = int(input("How many trees would you like to plant? "))
        print(f"Ok, we'll plant {number_of_trees} trees.")

    def display_info(self):
        print(f"You've just bought a house in {self.__area} with {self.__floor} floors ."
              f"Workers painted it {self.color}.")
        Home.trees(self)


house = Home("Slepyanka", "green", 3)
house.display_info()
house.color = "brown"
house.display_info()

