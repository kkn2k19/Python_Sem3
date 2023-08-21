# Write a program in python to input the lower and upper limit and print all the prime number lies between the range.
# Also print the following information 
# a. count number of prime numbers.
# b. count number of 2 digit prime number.

a = int(input("Lower Limit : "))
b = int(input("Upper Limit : "))
print("Prime Numbers in range ", a, " to ", b, " are --- ")
p = 0             #Total Prime Counter
t = 0             #Two Digit Prime Counter
for i in range(a, b+1):
    c = 0
    for j in range(2, i):
        if i%j==0:
            c=c+1
    if c==0:
        print(i, end=" ")
        p=p+1
        if i>9 and i<100:
            t=t+1
print("\nNumber of primes : ", p)
print("Two Digit Primes : ", t)
