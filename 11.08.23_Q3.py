# Sum of digits (Using While Loop)

n = int(input("Provide n : "))
i = n
s = 0
while (i > 0):
  d = i % 10
  s = s + d
  i = i/10
print("Sum of Digits : ", s)
