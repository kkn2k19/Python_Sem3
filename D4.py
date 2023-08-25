# Write a program in pyhton to calculate sum of digits of a given number using functions/ methods.

def sum_of_digits(n):
    s=0
    i=n
    while i>0:
        d=i%10
        s=s+d
        i=i//10
    print("Sum of Digits : ",s)

n=int(input("Enter n : "))
sum_of_digits(n)
