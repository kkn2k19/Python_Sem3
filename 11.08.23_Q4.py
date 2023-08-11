# Factorial of n

n = int(input("Provide n :"))
f = 1
i = n
while i>0 :
  d = i%10
  f = f*i
  i = i/10
print("Factorial of ", n, " = ", f)
