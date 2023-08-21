#  12345
#  2345
#  345
#  45
#  5

for i in range(1, 6):
    a=i
    for j in range(5-i+1):
        print(a, end="")
        a=a+1
    print()
