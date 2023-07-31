#A school has following rules for grading system : 
# a. below 25 - F
# b. 26 to 45 - E
# c. 46 to 50 - D
# d. 51 to 60 - C
# e. 61 to 80 - B
# f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.

marks = int (input ("Enter Marks : "))
if marks <= 25:
  print("Grade : F")
elif marks >= 26 and marks <= 45:
  print("Grade : E")
elif marks >= 46 and marks <= 50:
  print("Grade : D")
elif marks >= 51 and marks <= 60:
  print("Grade : C")
elif marks >= 61 and marks <= 80:
  print("Grade : B")
else :
  print("Grade : A")
