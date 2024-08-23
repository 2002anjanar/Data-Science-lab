Q.Create a two dimwnsional array with 4 rows and columns:
a. Display all elements excluding first row.
b. Display all elements excluding last column.
c. Display the elements of first and second column in second and third row.
d. Display elements of second and third column.
e. Display second and third element of first row.

___________________________________________

import numpy as np
arr=np.array([[2,3,8,11],[1,4,7,9],[8,5,0,7],[11,6,8,2]])
print(arr)
print(arr[1: , : ])
print(arr[ : , :3])
print(arr[1:3,0:2])
print(arr[ : ,1:3])
print(arr[ :1,1:3])

_____________________________________

OUTPUT:
[[ 2  3  8 11]
 [ 1  4  7  9]
 [ 8  5  0  7]
 [11  6  8  2]]

a. [[ 1  4  7  9]
    [ 8  5  0  7]
    [11  6  8  2]]

b. [[ 2  3  8]
    [ 1  4  7]
    [ 8  5  0]
    [11  6  8]]

c. [[1 4]
    [8 5]]

d. [[3 8]
    [4 7]
    [5 0]
    [6 8]]

e. [[3 8]]
