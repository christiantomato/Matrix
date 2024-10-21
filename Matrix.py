#identity matrix

rows = 5
columns = 5

matrix = []

#intialize the size of matrix
for i in range(rows):
    row = [0] * columns
    matrix.append(row)

#assign values to the identity
for i in range(rows):
    for j in range(columns):
       if i == j:
           matrix[i][j] = 1

#print the matrix
for i in range(rows):
    print(matrix[i])

