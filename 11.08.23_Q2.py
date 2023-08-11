# Sum of odd and even upto n

n = int(input("Provide n : "))
o = 0
e = 0
for i in range (1, n+1):
  if i%2 == 0 :
     e = e + i
  else :
    o = o + i
print("Sum of Even numbers : ", e)
print("Sum of Odd numbers : ", o)
    
