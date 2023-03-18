'''
Process of wrapping up of data and it's member in a single unit.
Class is a good example of encapsulation.
By use of encapsulation, restricts on accessing variable & methods from modification of data.
Python does not have the private keyword. Instead, it relies on the convention

private variables: To prevent accidental change, an objects variables can sometimes only be changed with an objects methods.
Protected members: Cannot be accessed outside the class but can be accessed from within the class and its subclasses.
starts with_
Private members: Accessible only in their own class/method. Neither be accessed outside the class nor by any base class.
starts with __
'''

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age
    def display(self):
        print(self.name)
        print(self._age)
person = Person('Dev', 30)
person.display()
print(person.name)
print('Trying to access variables from outside the class ')
print(person._age)

print("*"*50)

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
    def display(self):
        print(self.name)
        print(self.__age)
person = Person('Dev', 30)
person.display()
print('Trying to access variables from outside the class ')
print(person.name)
print(person.__age)

print("*"*50)

#Solution: Use of getter and setter
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
    def display(self):
        print(self.name)
        print(self.__age)
    def getAge(self):
        print(self.__age)
    def setAge(self, age):
        self.__age = age

person = Person('Dev', 30)
person.display()
person.setAge(45)
person.getAge()

