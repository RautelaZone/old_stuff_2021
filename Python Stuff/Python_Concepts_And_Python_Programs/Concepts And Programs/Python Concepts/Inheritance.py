'''
The method of inheriting the properties of parent class into a child class is known as inheritance
Benefits:
1) Code reusability
2) It represents a real world relationship between parent class and child class.
3) It is transitive in nature. If a child class inherits properties from a parent class,
then all other sub-classes of the child class will also inherit the properties of the parent class
'''

#Single Inheritance
class Parent:
    def func1(self):
        print("this is function one")
class Child(Parent):
    def func2(self):
        print("this is function 2 ")
print("Below is an example of Single Inheritance.")
ob = Child()
ob.func1()
ob.func2()
print("*"*50)

#Multiple Inheritance
class Parent:
    def func1(self):
        print("this is function 1")
class Parent2:
    def func2(self):
        print("this is function 2")
class Child(Parent, Parent2):
    def func3(self):
        print("this is function 3")
print("Below is an example of Multiple Inheritance.")
ob = Child()
ob.func1()
ob.func2()
ob.func3()
print("*"*50)

#Multilevel Inheritance
class Parent:
    def func1(self):
        print("this is function 1")
class Child(Parent):
    def func2(self):
        print("this is function 2")
class Child2(Child):
    def func3(self):
        print("this is function 3")
print("Below is an example of Multilevel Inheritance.")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()
print("*"*50)

#Hierarchical Inheritance
class Parent:
    def func1(self):
        print("this is function 1")
class Child(Parent):
    def func2(self):
        print("this is function 2")
class Child2(Parent):
    def func3(self):
        print("this is function 3")
print("Below is an example of Hierarchical Inheritance.")
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()
print("*"*50)
