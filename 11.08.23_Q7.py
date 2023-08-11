# Sum of digits (using for loop)

n = int(input("Provide n : "))
s = 0
for i in str(n):
  s = s + int(i)
print("Sum of Digits : ", s)
