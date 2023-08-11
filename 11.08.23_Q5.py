# Sum of factors of n

n = int(input("Provide n : "))
s = 0
for i in range (1, n+1):
  if n%i==0:
    s = s + i
print("Sum of Factors : ", s)
