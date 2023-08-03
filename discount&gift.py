#A cloth showroom has announced festival discounts, and the gifts on the purchase of items,
# Based on the total cost as given below:
# Total Cost               Discount               Gift
# upto 2000                  5%                  calculator
# 2001 to 5000               10%                 School Bag
# 5001 to 10000              15%                 wall clock
# above 10000                20%                 wrist watch

#Write a program to input the total cost. Compute and display the amount to be paid by the customer along with the gift.

total = float (input("Enter the total amount : "))
if total <= 2000:
  dis = 0.05*total
  gift = 'Calculator'
elif total >= 2001 and total <= 5000:
  dis = 0.1*total
  gift = 'School Bag'
elif total >= 5001 and total <= 10000:
  dis = 0.15*total
  gift = 'wall clock'
else :
  dis = 0.2*total
  gift = 'Wrist watch'
amount_payable = total - dis
print("Net Payable Amount : ", amount_payable)
print("Gift : ", gift)
