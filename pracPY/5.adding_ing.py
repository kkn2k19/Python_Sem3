#5. Write a Python program to add 'ing' at the end of a given String (length should be atleast 3). If the given String already ends with 'ing' then add 'ly' instead. If the String length of the given String is less than 3, leave it unchanged.

def add_string(str):
    length=len(str)
    if length>2:
        if str[-3:]=='ing':
            str+='ly'
        else:
            str+='ing'
    return str

str=input("Enter a String(Word) : ")
print("Final Word is ", add_string(str))
