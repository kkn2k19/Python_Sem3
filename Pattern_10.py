#  1
#  23
#  456
#  78910
#  1112131415

a=1
for i in  range(1, 6):
    for j in range(1, i+1):
        print(a, end="")
        a=a+1
    print()
