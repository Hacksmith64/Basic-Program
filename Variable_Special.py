from Module_Calc import Demo
print("India",__name__)
print("Hello")
print("Welcome User")
from Module_Calc import Sum

def Fun_1():
    Sum()
    print("From Fun_1")

def Fun_2():
    print("From Fun_2")

def Demo():
    Fun_1()
    Fun_2()

Demo()

