#Using loop
S = "geeksforgeeks"
L=[]
for i in S:
    if i not in L:
        L.append(i)
print("Unique Characters are:",L)
print("No of unique characters are:", len(L))

print("*"*50)

#By converting to set as set dont contain duplicate values
str="geeksforgeeks"
s = set(str)
print("Unique Characters are:",s)
print("No of unique characters are:",len(s))