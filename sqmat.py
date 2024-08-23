import numpy as np
matrix=np.random.randint(25,size=(2,2))
print("random matrix is:")
print(matrix)
print("Determinant of the Matrix:")
print(np.linalg.det(matrix))
print("Inverse of the Matrix:")
print(np.linalg.inv(matrix))
print("Rank of the Matrix:")
print(np.linalg.matrix_rank(matrix))
print("1 D array of matrix:")
print(matrix.flatten())

_____________________________________________________________________

                    OUTPUT

random matrix is:
[[ 3 23]
 [20 11]]
Determinant of the Matrix:
-426.9999999999997
Inverse of the Matrix:
[[-0.02576112  0.05386417]
 [ 0.04683841 -0.00702576]]
Rank of the Matrix:
2
1 D array of matrix:
[ 3 23 20 11]
