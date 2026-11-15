# Oops is majorly used to remove redundancy and increase reusability of the code
# Before creating an object , its class is created and then object is added

# class is a blueprint for creating object that stores all the features of object( saves info )
# class Student:                                               # creation of a class
#     name="Mridul Joshi"

# objects represent the individual students of the class 
# (object variable) s1=Student()                                                 # creation of an object

# print(s1.name);

# s2=Student()
# print(s2.name)
     


class cars:
    type="sedan"
    def __init__(self):                                           # default constructor
        pass

    def __init__(self,brandname,colorname):                       # parameterized constructor 

        self.name=brandname
        self.color=colorname

        print("adding new car in database..")
    
    @staticmethod                                               # decorator
    def hello():
        print("kese ho dosto")

    def welcome(self):                                                                  # new method created
        print("welcome to our car showroom , this car color is ",self.color)
    

car1=cars('Mercedes',"black")                                      # element 1
print(car1.name)
print(car1.color)
print(car1)
car1.welcome()                             # new method call

car2=cars('bmw','blue')                                            # element 2
print(car2.name)
print(car2.color)
print(car2)
car2.welcome()                             # new method call

# jo cheez common hoti hai apne har element ke data me uske liye ham har baar different objects me again again nahi likhte as it occupies space , rather we create a class attribute and store it 
print(cars.type) # as it is common for all

# object attribute > class attribute ( when same name ke attributes created ho both sides )

# for creating new method --> def method__name(self,parameters):
#                                 print("hello",self.method)


# Static method --> methods that do not uses self parameter
cars.hello()     # works at class level , not at object level