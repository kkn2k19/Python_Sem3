# Print Number Pattern

n = int (input ("No. of lines : "))
for i in range (1, n+1):
  for j in range (1, i+1):
    print(j, end=" ")
  print()
