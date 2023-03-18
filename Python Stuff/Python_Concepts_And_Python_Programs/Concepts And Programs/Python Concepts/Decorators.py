'''
Decorators allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
without permanently modifying it.
'''

def decorator_fun(func):
    print("Inside decorator")
    def inner():
        print("Inside inner function")
        print("Decorated the function")
        # do operations with func
        func()
    return inner

@decorator_fun
def func_to():
    print("Inside actual function")
func_to()

print("*"*50)

def helloDecorator(func):
    def inner():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner

def function_to_be_used():
    print("This is inside function")

function_to_be_used = helloDecorator(function_to_be_used)
function_to_be_used()


