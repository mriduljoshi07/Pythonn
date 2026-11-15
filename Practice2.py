# write a code in python basically explaining inheritance of attributes and methods of a car starting color,accelerating , breaking with another car named toyota inheriting these 

# class car:
#     def __init__(self, color):
#         self.color = color
#         self.speed = 0

#     def accelerate(self, amount=10):
#         self.speed += amount
#         return f"Accelerating to {self.speed} km/h"

#     def brake(self):
#         self.speed = 0
#         return "Car has stopped"

#     def show_color(self):
#         return f"Car color is {self.color}"

# class toyota(car):
#     pass


# my_toyota = toyota("red")

# print(my_toyota.show_color())
# print(my_toyota.accelerate())
# print(my_toyota.brake())

# explain inheritance to me using an easy example
class Vehicle:
    def move(self):
        print("Vehicle can move")

class Car(Vehicle):
    def honk(self):
        print("Car honks")

my_car = Car()
print(my_car.move())
print(my_car.honk())
   
