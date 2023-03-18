'''
Polymorphism means same function name (but different signatures) being uses for different types.
Method Overriding is the concept in Polymorphism
'''

def add(x, y, z=0):
    return x + y + z
# Driver code
print(add(2, 3))
print(add(2, 3, 4))