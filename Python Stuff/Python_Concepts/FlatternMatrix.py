'''
Flattern Matrix is like separating each individual
Input: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
Flattern Matrix is : [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

#using FOR loop
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = []
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)

#Using List Comprehension
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)