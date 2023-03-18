'''
First Class Objects means that functions can be used as arguments or passed as arguments.
Properties of FCF:
A function is an instance of the Object type.
You can store the function in a variable
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists etc
'''

#Treating the functions as objects.
def shout(text):
    return text.upper()

print(shout('Hello'))
yell = shout
print(yell('Hello'))

#Passing the function as argument
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)
greet(shout)
greet(whisper)

#Returning functions from another functions.
def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_15 = create_adder(15)
print(add_15(10))