# Write a program in python to check whether a givennumber  is prime or not using functions/ methods.

def prime_check(n):
    flag=0
    for i in range(2, n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print("Prime Number.\n")
    else :
        print("Not a Prime Number.\n")

n=int(input("Enter n : "))
prime_check(n)
