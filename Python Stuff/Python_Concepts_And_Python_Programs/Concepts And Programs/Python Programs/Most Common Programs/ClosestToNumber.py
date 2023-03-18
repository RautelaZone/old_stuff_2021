# import numpy as np
#
# arr = np.array([1, 2, 8, 4, 5])
# value = 0
#
# absolute_val_array = np.abs(arr - value)
# smallest_difference_index = absolute_val_array.argmin()
# closest_element = arr[smallest_difference_index]
#
# print("Closest element to" ,value, "is:", closest_element)

# N = 5
# A = [5,4,1,2,3,9]
# No = 0
#
# new = []
# A.sort()
#
# for items in A:
#     D = abs(items-No )
#     new.append(D)
#
# print(new[0])

mylist = [1, 2, 3, 4, 5, 6, 7, 9, 10]
mynumber = int(input("enter num : "))

def closest(list, Number):
    temp = []
    for i in list:
        temp.append(abs(Number-i))

    return temp.index(min(temp))

a = closest(mylist, mynumber)
print ("index is : ",a)
print ("Closet value is : ",mylist[a])