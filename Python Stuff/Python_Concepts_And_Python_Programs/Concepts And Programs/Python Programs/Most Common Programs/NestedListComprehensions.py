
'''
Output matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
'''

#Method-1
matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

#Using Nest List Comprehension
matrix = [ [j for j in range(5)] for i in range(5)]
print(matrix)




matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = [i for item in matrix for i in item ]
print(flatten_matrix)