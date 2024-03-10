n=int(input("Enter n : "))

c=0
for i in range(2, n):
    if n%i==0:
        c=c+1
        break
if c==0 and n>1:
    print("Prime Number")
else:
    print("Not a prime Number")


print("Factors of ", n, " : ")
for i in range(1, n+1):
    if n%i==0:
        print(i, end=" ")

print("\nSum of digits of ", n, " : ")
s=0
i=n
while i>0:
    d=i%10
    s=s+d
    i=i//10
print(s)


print("\nReverse of ", n, " : ")
i=n
r=0
while i>0:
    d=i%10
    r=r*10+d
    i=i//10
print(r)

print("\nFactorial of ", n, " : ")
f=1
for i in range(1, n+1):
    f=f*i
print(f)



