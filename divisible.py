#Write a program to accept a number and check whether the number is divisible by 3 as well as 5. Otherwise, decide:
# (a) Is the number divisible by 3 and not by 5?
# (b) Is the number divisible by 5 and not by 3?
# (c) Is the number neither divisible by 3 nor by 5?
# The program displays the message accordingly.

a = int (input("Enter a number : "))
if a%3 == 0 and a%5 == 0:
  print("Divisible by both 3 as well as 5.")
elif a%3 == 0:
  print("Divisible by 3 and not by 5.")
elif a%5 == 0:
  print("Divisible by 5 and not by 3.")
else :
  print("Not divisible by 3 as well as 5.")
