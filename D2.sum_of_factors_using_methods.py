# Write a program in python to calculate sum of factors of a number using functions/ methods.

def sum_of_factors(n):
    s=0
    for i in range(1, n+1):
        if n%i==0:
            s=s+i
    print("Sum of Factors : ", s)

n=int(input("Enter n : "))
sum_of_factors(n)
