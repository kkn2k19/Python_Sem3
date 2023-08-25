# Write a program in python to calculate factorial of a number using functions/ methods.

def fact(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    print("Factorial : ", f)

n=int(input("Enter n : "))
fact(n)
