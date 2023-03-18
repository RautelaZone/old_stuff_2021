'''
Finding Intersection using Lambda Dunction or
Finding Common values
'''

def interSection(arr1, arr2):
    result = list(filter(lambda x: x in arr1, arr2))
    print("Intersection values are:",result)

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
interSection(arr1, arr2)