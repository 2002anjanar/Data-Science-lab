import numpy as np
ar1=np.array([[1,4],[2,6]])
ar2=np.array([[10,5],[8,3]])
print("first matrix: \n",ar1)
print("second matrix: \n",ar2)
print("matrix addition:")
print(np.add(ar1,ar2))
print("matrix subtraction:")
print(np.subtract(ar1,ar2))
print("multiplication of individual elements:")
print(np.multiply(ar1,ar2))
print("matrix division:")
print(np.divide(ar1,ar2))
print("matrix multiplication:")
print(np.dot(ar1,ar2))
print("transpose of matrix1:")
print(ar1.transpose())
print("transpose of matrix2:")
print(ar2.transpose())
print("sum of diagonal elements of matrix1:")
print(np.trace(ar1))
print("sum of diagonal elements of matrix2:")
print(np.trace(ar2))

___________________________________________________________________________

       OUTPUT
first matrix: 
 [[1 4]
 [2 6]]
second matrix: 
 [[10  5]
 [ 8  3]]
matrix addition:
[[11  9]
 [10  9]]
matrix subtraction:
[[-9 -1]
 [-6  3]]
multiplication of individual elements:
[[10 20]
 [16 18]]
matrix division:
[[0.1  0.8 ]
 [0.25 2.  ]]
matrix multiplication:
[[42 17]
 [68 28]]
transpose of matrix1:
[[1 2]
 [4 6]]
transpose of matrix2:
[[10  8]
 [ 5  3]]
sum of diagonal elements of matrix1:
7
sum of diagonal elements of matrix2:
13
