'''
Find Union
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
Output: 1 2 3 4 5 6 7
'''

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
arr1.sort()
arr2.sort()

def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i],end=" ")
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j],end=" ")
            j += 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1
    while i < m:
        print(arr1[i],end=" ")
        i += 1
    while j < n:
        print(arr2[j],end=" ")
        j += 1

printUnion(arr1, arr2, m, n,)