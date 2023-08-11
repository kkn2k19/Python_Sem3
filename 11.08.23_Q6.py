# Palindrome Number

n = int(input("Provide n : "))
r = 0
i = n
while i>0:
  d = i%10
  r = r*10 + d
  i = i/10
if r == n:
  print("Palindrome Number.")
else :
  print("Not a Palindrome Number.")
