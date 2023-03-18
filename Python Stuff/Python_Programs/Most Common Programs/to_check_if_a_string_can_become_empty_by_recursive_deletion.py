'''
Question: String slicing in Python to check if a string can become empty by recursive deletion
Given a string “str” and another string “sub_str”.
We are allowed to delete “sub_str” from “str” any number of times.
It is also given that the “sub_str” appears only once at a time.
The task is to find if “str” can become empty by removing “sub_str” again and again.
'''

def checkSub(input, pattern):
    if len(input) and len(pattern)==0:
        return True
    if len(pattern)==0:
        return True
    while len(input)!=0:
        index = input.find(pattern)
        if index==-1:
            return False
        input = input[0:index] + input[index + len(pattern):]
    return True

input="GEEGEEKSKS"
pattern="GEEKS"
print(checkSub(input,pattern))