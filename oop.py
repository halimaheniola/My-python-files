# classes : instance/object/instantiation senior colleagues to functions
#classes is blueprint while an object is an instance of a class
# methods
#  -static method
#  -class method
#  -instance method
#  -magic method
#inheritance
#polymorphism
#Abstraction
# ClassProduct sentence case naming convention for a class
#class attributes


class Customer():
    def __init__(self, name):
        self.name = name
    def set_balance(self, balance):
        self.balance = balance
        return None
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if not amount > self.balance:
            self.balance -= amount
        else:
            raise RuntimeError("Insufficient Balance")
        return self.balance
    def get_balance(self):
        return self.balance
        
# new_customer = Customer("James")
#print(new_customer.name)
# new_customer.set_balance(25000)
#print(new_customer.get_balance())
# new_customer.deposit(50000)
#print (new_customer.get_balance())
# new_customer.withdraw(30000)
# new_customer.get_balance()


class Vehicle():
    def __init__(self, kind, no_of_wheels, year_of_manufacture, cost, speed = 0):
        self.kind = kind
        self.year_of_manufacture = year_of_manufacture
        self.cost = cost
        self.no_of_wheels = no_of_wheels
        self.speed = speed
    def can_fly(self):
        return self.kind == "Aeroplane"
    def accelerate(self, value):
        self.speed +=value
        return self.speed
    def can_sail(self):
        return self.kind =="ship"
class Car(Vehicle):
    pass



import math
"""class ShapesCalculator(object):
    def __init__(self, name, radius, length, breadth, base, height, area):
        self.name = name
        self.radius = radius
        self.length = length
        self.breadth = breadth
        self.area = area
        self.base = base
        self.height = height
        
    def circle(self):
        area += (math.pi * float(self.radius **2))
        return self.area
    def triangle(self,):
        area = (float(0.5) * float(self.base) * float(self.height))
        return self.area
    def rectangle(self):
        area = (self.length * self.breadth)
        return self.area
    def square(self):
        area = (self.length **2)
        return self.area
    def cone(self):
        area += (float(0.5) * float(self.base + self.base) * float(self.height))"""
# 1 create class using the class keyword
#2 instantiate the class i.e create an object from the class
# 3 perform action on the object  created
# such as calling the methods defined in the class


class ShapesCalc(object):
 pi = 3.142
 def __init__(self):
    pass
 def triangle(self, base, height):
     return 0.5 * base * height
 def circle(self, radius):
     return self.pi * radius **2
 def square(self, length, breadth):
     return length * breadth
 def rectangle(self, lenght, breadth):
     return length * breadth
                                        
