# =========================================
# OOPS(object oriented programming) Part2
# =========================================

# del keyword(use to delete object property and object itself)

# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Anus")
# del s1

# private(like) attridutes and methods

# class Account:
#     def __init__(self,account_no,password):
#         self.__acc=account_no #self.acc=account_no => self.__acc=account_no (private now)
#         self.__passw=password

#     def reset_pass(self):
#         print(self.__passw)

# acc1=Account("1234","abcd")
# print(acc1.reset_pass())

# 1 more pillar of OOPS
# 4.inheritance (when one class(child/parent) derives the property & method of anothr class(parent/base).)
# class Car:
#     def __init__(self):
#         self.accelator=False
#         self.brake=False
#         self.clutch=False

#     def Start(self):
#         self.accelator=True
#         self.clutch=True
#         print("Car Started")
# class Toyota_Car(Car):
#     def __init__(self,name):
#         self.name=name

# car1=Toyota_Car("Fortuner")
# car2=Toyota_Car("Defender")
# print(car1.Start())

# super method (method is used to methods class)

# class Car4:
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Toyota_Car2(Car4):
#     def __init__(self,name,type):
#         self.brand=name
#         super().__init__(type)

# t_c1=Toyota_Car2("Defender","electric")
# print(t_c1.type)

# @classmethod 

# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=Person()
# p1.changeName("Huzaifa")
# print(p1.name)
# print(Person.name)

# @property

# class Student2:
#     def __init__(self,eng,urdu,math):
#         self.eng=eng
#         self.urdu=urdu
#         self.math=math

#     @property
#     def percentage(self):
#             return str((self.eng+self.math+self.urdu)/3)+"%"

# stu1=Student2(89,98,91)
# stu1.eng=98
# print(stu1.percentage)
"""
# 1 more pillar of OOPS
# -------------------------------------
# 4.polymorphism(when the same operator have different meaning in different sitiuyion)
# -------------------------------------
# dender functions
# __add__ , __sub__ ,etc...
class Complex():
    def __init__(self,real,imaginary):
        self.real=real
        self.img=imaginary

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(5,6)
num2.showNumber()

num3=num1 - num2
num3.showNumber()
"""
# practice 1
# class Circle:
#     def __init__(self,radius):
#         self.r=radius
#     def Area(self):
#         print("The area of circle is",3.14*self.r**2)
#     def Perimeter(self):
#         print("The radius of circle is",2*3.14*self.r)
# input=int(input("Enter a radius of circle: "))
# circle1=Circle(input)
# circle1.Area()
# circle1.Perimeter()

# Practice2
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.d=department
#         self.salary=salary

#     def showDetail(self):
#         print(self.d)
#         print(self.role)
#         print(self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Web developer","IT","165000")

# engineer1=Engineer("Anus Khan",35)
# engineer1.showDetail()

# Practice 3
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, order2):
        return self.price>order2.price

order1=Order("chips",20)
order2=Order("Tea",15)
print(order1>order2)