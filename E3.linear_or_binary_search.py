# Write a program to input integer values in a list and perform Linear Search or Binary Search. Also display the position of the number in the list.

def LinearSearch(arr, se):
    for i in range(0, n):
        if arr[i]==se:
            return i
    return -1

def BinarySearch(arr, se):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if se==arr[mid]:
            return mid
        if se>arr[mid]:
            start=mid+1
        else :
            end=mid-1
    return -1

n=int(input("Enter size of List : "))
arr=[]
for i in range(0, n):
    k=int(input("Enter value : "))
    arr.append(k)
print("Original List : ", arr)
choice=input("Enter L for Linear Search or B for Binary Search : ")
se=int(input("Enter Search Element : "))
if choice=='L':
    index=LinearSearch(arr, se)
elif choice=='B':
    arr.sort()
    index=BinarySearch(arr, se)
else :
    print("Invalid Choice! Enter either L or B only.\n")
if index==-1:
    print("Not Found\n")
else:
    print("Found at index : ", index)




















