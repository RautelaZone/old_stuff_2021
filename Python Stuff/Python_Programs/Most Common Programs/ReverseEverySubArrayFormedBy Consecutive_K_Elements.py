'''
Question: Reverse an array in groups of given size .
Given an array, reverse every sub-array formed by consecutive k elements.

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
Result: [3, 2, 1, 6, 5, 4, 9, 8, 7]
'''

def reverseGroup(a, k):
    res = []
    for i in range(0, len(a), k):
        res.extend((a[i:i + k])[::-1])
    print(res)

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
reverseGroup(input, k)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
r=[]
for i in range(0,len(arr),k):
    r.extend((arr[i:i + k])[::-1])
print(r)