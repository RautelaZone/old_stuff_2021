'''
Find Intersection
Intersection: Common Items
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
Output: 2 5
'''

#Normal Method
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
arr1.sort()
arr2.sort()

def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1
printIntersection(arr1, arr2, m, n)

#Using Lambda Function
def interSection(arr1, arr2):
    result = list(filter(lambda x: x in arr1, arr2))
    print("Intersection : ", result)

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
interSection(arr1, arr2)