# class Student:
#     name='romero';

# s1=Student();
# print("hey",s1.name)

class student:
    def __init__(self,name,std,age):
        self.name=name
        self.std=std
        self.age=age

    @staticmethod
    def noty():
        print("bubbly horha hai")

s1=student("john",10,25);
print(s1.name)
print(s1.std)
print(s1.age)
print(s1)
s1.noty()