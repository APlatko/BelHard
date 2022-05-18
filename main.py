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


mercedes = Car(1, 1, 1, 20)
mercedes.reversal()
mercedes.speed_increase()
mercedes.speed_actual()
mercedes.speed_increase()
mercedes.reversal()
mercedes.speed_actual()
print(mercedes.speed_actual())
mercedes.speed_increase()
print(mercedes._Car__speed)


