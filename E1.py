# Write a Python program to remove duplicates from an integer list (Elements supplied by the user).
# Find 2nd largest number from the list.

def remove_duplicate(arr):
  print("List after removing duplicates : ")
  for i in range(0, n):
    c=0
    for j in range(i+1, n):
      if arr[i]==arr[j]:
        c=1
        break
    if c==0:
      print(arr[i], end=" ")

def second_largest(arr):
  for i in range(0, n):
    for j in range(i+1, n):
      if arr[i]>arr[j]:
        arr[i]=arr[j]
  print("Second Largest Number from List : ", arr[n-2])

n=int(input("Enter no. of elements : "))
arr=[]
for i in range(1, n+1):
  k=int(input("Enter value : "))
  arr.append(k)
print("original List : ", arr)
second_largest(arr)
remove_duplicate(arr)
