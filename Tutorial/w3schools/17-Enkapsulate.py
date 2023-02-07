class Car:
    def __init__(self):
        self.__speed = 0
    def set_speed(self, speed):
        if(speed >= 0):
            self.__speed = speed
        else:
            self.__speed = 0
    def get_speed(self):
        return self.__speed

car = Car()
car.set_speed(60)
print(car.get_speed())