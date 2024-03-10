#4. Write a python program to find the maximum frequency of a character in a given String.

def max_freq(str1):
    ASCII_SIZE=256
    ctr=[0]*ASCII_SIZE
    max=-1
    ch=''
    for i in str1:
        ctr[ord(i)]+=1
    for i in str1:
        if max<ctr[ord(i)]:
            max=ctr[ord(i)]
            ch=i
    print("Character is ", ch, "\nFrequency is ", max)

str=input("Enter a  String : ")
max_freq(str)
