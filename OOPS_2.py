# Pillars of OOPs
# 1) Abstraction 
# 2) Encapsulation
# 3) Inheritance    
# 4) Polymorphism

# Create a class named account with parameters as balance and account no which has methods to debit , credit and check the balance 
# class Account:
#     def __init__(self,account_no,bal,acc_pass):
#         self.acc_no=account_no
#         self.balance=bal
#         self.__password=acc_pass

#     def reset_pass(self,old_pass,new_pass):
#         if old_pass==self.__password:
#             print("Thank you for the confirmation , type your new password ! ")
#             self.__password==new_pass
#             print("password has been changed :)")
#         else:
#             print("Wrong password entered !")

#     def debit(self,amount):
#         if amount>self.balance:
#             print("Insufficient balance , cant withdraw !")
#         else:
#             self.balance=self.balance-amount
#             print(amount," has been debited successfully !")
    
#     def credit(self,amount):
#         self.balance=self.balance+amount
#         print(amount," has been credit in you bank account no: ",self.acc_no)
    
#     def bank_bal(self):
#         print("Dear user, your bank account stated ",self.acc_no," has curently ",self.balance," as balance")

# s1=Account(98992,32,"jai mridul");
# s1.credit(47)
# s1.debit(56)
# s1.bank_bal()
# print(s1.balance)       # as accessed outside the scope of its class , toh basically public 
# print(s1.balance)       # as accessed outside the scope of its class , toh basically public 
# print(s1.acc_no)

# print(s1.password)      # this type of sensitive data should be private not public as it can be changed by public
# print(s1.__password)    # this is now set to be private and cant be accessed outside the class and hence will give " no such attribute " as error
# s1.reset_pass("jai mridul","jai ho")


# del keyword --> when we create an object it occupies memory and space , so this keyword help to permanently remove a particular object and its properties
# for a particular property/attribute ---> del s1.acc_no
# for an object ---> del s1

# class MAIT:
#     __name="Mridul joshi"
#     color="white"
#     gender="male"
#     __branch="aiml"

# r=MAIT()
# print(r.gender)
# print(r.__name)                               # by this way class attributes can be made private

# Even the functions of the class can be made private and can only be accessed through class internal functions


# Inheritance
class Employee:
    def __init__(self,name,id,gender):
        self.name=name
        self.id=id
        self.gender=gender

    def details(self):
        print(f"the name of the employee is {self.name} and the id is {self.id} and specified as {self.gender}")
    
class programmer(Employee):
    def lang(self):
        print("we programmers love python")
        

e1=Employee("manan",234,"male")
e1.details()
e2=programmer("mridul",200,"male")    # now e2 has features of both classes hence it can access both functions
e2.details()
e2.lang()
print("---------------------------------------------------------")
e3=programmer("india",1,"female")
e3.lang()
e3.details()
