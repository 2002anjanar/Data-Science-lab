x=int(input("enter the 1st number"))
y=int(input("enter the 2st number"))
if x>y:
    x,y=y,x
for i in range(1,x+1):
    if x%i==0 and y%i==0:
        gcd=i
print("Gcd of",x,"and",y,"is",gcd)
------------------------------------
OUTPUT

enter the number of elements:4
Enter elements 1: 8
Enter elements 2: 3
Enter elements 3: 6
Enter elements 4: 1
the array is :[8, 3, 6, 1]
Sorted array is: [1, 3, 6, 8]
