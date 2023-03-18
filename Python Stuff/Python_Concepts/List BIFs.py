'''
Source: https://www.geeksforgeeks.org/python-list/
'''

List = ["Anil", "Rautela", 1,2.5,"Str", 'Pintoo', 3.14,15,"Anil"]

List.append("Appended Word")
print("After append, List is:",List)

List.extend("E")
print("After Extend a word, List is:",List)

List.extend(["Extended Word"])
print("After Extend a List, List is:",List)

List.insert(1,"Hero")
print("After Insert 'Hero' at index 1, List is:", List)

List.remove("Hero")
print("After Removing 'Hero' word, List is:", List)

List.pop()
print("After POP, POP will remove last value so, List is:", List)

List.pop(3)
print("This will pop value at index 3, List is:", List)

#List.index("Anil")
print("Returns the index of the first matched item, List is:", List.index("Anil"))

List.count("Anil")
print("Count of Anil in List is:",List.count("Anil"))

List.clear()
print("After clearing all values, List is:", List)

List1 =[100,105,150,201]
print("Sum of items in List1 is:",sum(List1))







