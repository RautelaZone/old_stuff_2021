
# Using in
def subInString(s1, s2):
    if s2 in s1:
        print("Substring is a part of String. ")
    else:
        print("Substring is not a part of String. ")

s1 = input("Enter a string: ")
s2 = input("Enter a substring: ")
subInString(s1, s2)

#Using find
def check(s1, s2):
    if (s1.find(s2) == -1):
        print("Substring is not a part of String. ")
    else:
        print("Substring is a part of String. ")

s1 = input("Enter a string: ")
s2 = input("Enter a substring: ")
check(s1, s2)

#Using count
def check(s2, s1):
    if (s2.count(s1) > 0):
        print("Substring is a part of String. ")
    else:
        print("Substring is not a part of String. ")

s2 = input("Enter a string: ")
s1 = input("Enter a substring: ")
check(s2, s1)