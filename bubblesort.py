arr=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    arr.append(int(input(f"Enter elements {i+1}: ")))
print(f"the array is :{arr}")
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Sorted array is:",arr)

---------------------------------------------------------

OUTPUT

enter the number of elements:5
Enter elements 1: 70
Enter elements 2: 20
Enter elements 3: 10
Enter elements 4: 40
Enter elements 5: 50
the array is :[70, 20, 10, 40, 50]
Sorted array is: [10, 20, 40, 50, 70]
