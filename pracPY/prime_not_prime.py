n=int(input("Enter n : "))
print("\nSum of digits of ", n, " : ")
s=0
i=n
while i>0:
    d=i%10
    s=s+d
    i=i//10
print(s)
