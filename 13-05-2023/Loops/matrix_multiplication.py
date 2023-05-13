# Matrix multiplication

matrix1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
matrix2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# size of matrix
rows1 = len(matrix1)
cols1 = len(matrix1[0])
rows2 = len(matrix2)
cols2 = len(matrix2[0])

# check if matrix multiplication is possible
if cols1 != rows2:
    print("Matrix multiplication is not possible")
else:
    # create a result matrix
    result = [[0 for i in range(cols2)] for j in range(rows1)]
    print(result)
    
    # multiply the matrices
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    # print the result
    for r in result:
        print(r)
