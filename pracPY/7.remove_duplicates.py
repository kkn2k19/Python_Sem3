#7. Write a Python program to remove duplicates from an integer list (Elements supplied by the user).
#   Find 2nd largest number from the list.

def remove_duplicate(arr):
    unique_arr=[]
    for i in range(0, n):
        c=0
        for j in range(i+1, n):
            if arr[i]==arr[j]:
                c=1
                break
        if c==0:
            unique_arr.append(arr[i])
    return unique_arr

def second_largest(unique_arr):
    m=len(unique_arr)
    for i in range(0, m):
        for j in range(i+1, m):
            if unique_arr[i]>unique_arr[j]:
                unique_arr[i]=unique_arr[j]
    return unique_arr[m-2]

n=int(input("Enter no. of elements : "))
arr=[]
for i in range(1, n+1):
  k=int(input("Enter value : "))
  arr.append(k)
print("original List : ", arr)
unique_arr=remove_duplicate(arr)
print("List after Removing Duplicates : ", unique_arr)
print("Second Largest Number from List : ", second_largest(unique_arr))
