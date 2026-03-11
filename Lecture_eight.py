# ------------------------------------
# OOPS (object oriented programming)
# ------------------------------------

# class Students:
#     name="Anus"

# st=Students()
# print(st.name)

# class Car:
#     color="red"
#     brand="mercedes"

# c1=Car()
# print(c1.color)
# print(c1.brand)

# __init__ function (constructor function) in OOPS

# class Students2:

#     # default constructor
#     def __init__(self):
#         pass

#     # Parameterized constructor
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.mark=marks
#         print("adding new student in Database...")

# st2=Students2("Anus",23)
# print(st2.name)
# st2b=Students2("Huzaifa",45)
# print(st2.mark)

# Attributes in class and instance

# instance (obj.attr) It is different for every object

# class Students3:
#     def __init__(self,fullname,marks):
#         self.name=fullname #self.name => instance (obj.attr)
#         self.mark=marks
#         print("adding new student in Database...")

# Class (Class.attr) which thing is common we create their class atribute


# class Student4:
#     college_Name = "ABC College"  # this college name is common for all objects,so we make its Class now no matter how many objects formed but it stored only once
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.mark=marks
#         print("adding new student in Database...")

# st4=Student4("Anus",99)
# print(st4.college_Name)

# Class is a collection of 2 things attributes(data[we learn priviously]) and methods

# Class Methods(Methods are functions that belong to obj)

# class Class_Methods:
#     college_Name = "ABC College"  
#     def __init__(self,fullname,marks):
#         self.name=fullname 
#         self.mark=marks
#                         #----
#     def welcome(self):      #   |--method
#         print("welcome",self.name)#   |
#                         #----
# st_CL=Class_Methods("Anus",99)
# st_CL.welcome()

# class Practice_1:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def average(self):
#         sum=0
#         for item in self.marks:
#             sum+=item
#         print("hi",self.name,"your average marks is",sum/3)

# Practice_1_a=Practice_1("Anus",[94,89,91])
# Practice_1_a.average()

# static method (method that do not use static method)

# class static:
#     @staticmethod
#     def hello():
#         print("hello")

# ----------------------
# 2 main pillar of OOPS
# ----------------------

# 1. Abstraction(hiding a impletation of class and only show important feature to user)

# class Car2:
#     def __init__(self):
#         self.accelator=False
#         self.brake=False
#         self.clutch=False

#     def Start(self):
#         self.accelator=True
#         self.clutch=True
#         print("Car Started")

# car_2=Car2()
# car_2.Start() #we does not see any thing which internaly implement in class from outside of Class.

# 2.Encapsulation (Wraping data and function into a single unit/object.)


# All code we write above is Encapsulation

# practice_2:

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"succesfully debited.")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"succesfully credited.")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,45237)
print("1. See balance")
print("2. Add balance")
print("3. Debited balance")
choice=int(input("Choose your number:"))
if(choice==1):
    print("total balance=",acc1.get_balance())
elif(choice==2):
    input2=int(input("Add amount:"))
    acc1.credit(input2)
elif(choice==3):
    input3=int(input("debited amount:"))
    acc1.debit(input3)