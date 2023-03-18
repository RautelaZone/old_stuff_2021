'''
Global keyword is a keyword that allows a user to modify a variable outside of the current scope.
It is used to create global variables from a non-global scope i.e inside a function.
'''
a=1
def f():
    print('Inside f() : ', a)
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

print("*"*50)

# global variables
a = 15
b = 10
def add():
    c = a + b
    print(c)
add()

print("*"*50)

a = 15
def change():
    global a
    a = a + 5
    print(a)
change()

print("*"*50)

def add():
    x = 15
    def change():
        global x
        x = 20
    print("Before making changing: ", x)
    print("Making change")
    change()
    print("After making change: ", x)
add()
print("value of x", x)