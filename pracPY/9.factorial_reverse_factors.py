# 2 . Write a menu driven program in python which will accept a number and choice as ‘a’,’b’,’c’ from the user and
#     calculate the following according to the user choice.(use user defined function):
#     a.	Factorial of each digit (Calculate factorial of each digit and return the the same).
#     b.	Reverse of that number (Calculate Reverse of the number and display) 
#     c.	Factor’s of that number (Display factors of the number)

choice = input("Enter 'a' for Factorial of each digit.\n'b' for Reverse of Number.\n'c' for Displaying Factors of a Number. : ")
n=int(input("Enter n : "))

if choice == 'a':
    i=n
    while i>0:
        d=i%10
        f=1
        for k in range(1, d+1):
            f=f*k
        print("Factorial of ", d, " : ", f)
        i=i//10

elif choice=='b':
    r=0
    i=n
    while i>0:
        d=i%10
        r=r*10+d
        i=i//10
    print("Reverse of ", n, " : ", r)

elif choice=='c':
    print("Factors of ", n, " : ")
    for i in range(1, n+1):
        if n%i==0:
            print(i, end=" ")
