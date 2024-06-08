# Encapsulation example
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.__speed = 0  # Encapsulated attribute

    def accelerate(self, increment):
        self.__speed += increment

    def get_speed(self):
        return self.__speed

my_car = Car("Toyota")
my_car.accelerate(20)
print(my_car.get_speed())  # Output: 20
