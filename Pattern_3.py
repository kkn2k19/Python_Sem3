#  54321
#  5432
#  543
#  54
#  5

for i in range (1, 6):
    a = 5
    for j in range(6-i, 0, -1):
        print(a, end="")
        a=a-1
    print()
