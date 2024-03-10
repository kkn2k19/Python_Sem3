#8. Program to determine whether a given number is a happy number.
#   The happy number can be defined as a number which will yield 1 when it is replaced by the sum of the square of its digits repeatedly. 
#   If this process results in an endless cycle of numbers containing 4, then the number is called an unhappy number.(use math module)
#   For example, 32 is a happy number as the process yields 1 as follows
#    3^2 + 2^2 = 13
#    1^2 + 3^2 = 10
#    1^2 + 0^2 = 1

n = int(input("Enter n : "))
sum = n
while sum>9:
    n = sum
    sum = 0
    while n>0:
        d = n%10
        sum = sum+d*d
        n=n//10
if sum==1:
    print("Happy Number.")
else :
    print("Not a Happy Number.")
