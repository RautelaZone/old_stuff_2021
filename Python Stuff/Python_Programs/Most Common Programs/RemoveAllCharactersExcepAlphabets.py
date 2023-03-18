'''
Removing all characters except alpbhabets
'''

#Using FOR loop
input = "$Gee*k;s..fo, r'Ge^eks?"
for char in input:
    if ord(char) in range(ord('a'),ord('z')+1,1) or ord(char) in range(ord('A'),ord('Z')+1,1):
        result=char
        print("".join(result),end="")


#Using List Comprehension
input = "$Gee*k;s..fo, r'Ge^eks?"
result=[char for char in input if ord(char) in range(ord('a'),ord('z')+1,1) or ord(char) in range(ord('A'),ord('Z')+1,1)]
print("".join(result),end="")
