#A company divided salary in 4 slabs:
# Grade     Basic(Rs. per month)        DA(% of Basic)        HRA(% of Basic)
# 1         10000 or more                    40%                    30%
# 2         5000 - 10000                     40%                    25%
# 3         <5000 but >2000                  30%                    20%
# 4         2000 or less                     30%                    15%
#If the salary which is the total of basic, DA and HRA is above Rs. 50000 per month then 
#Income tax at the rate of 30% of the annual salary exceeding 50000 is deducted on monthly basis at source. 
#Taking name of the employees and the basic (monthly) pay as inputs, 
#a pay slip, which contains Name, Basic monthly pay, DA, HRA, monthly Income Tax and Net monthly Salary. 
#Write a program to perform this job. 

name = input("Enter employee name : ")
basic = float (input ("Enter basic salary : "))
it = 0
netsal = 0
if basic >= 10000:
  da = basic*0.4
  hra = basic*0.3
elif basic >= 5000 and basic < 10000:
  da = basic*0.4
  hra = basic*0.25
elif basic > 2000 and basic < 5000:
  da = basic*0.3
  hra = basic*0.2
else :
  da = basic*0.3
  hra = basic*0.15
salary = basic + da + hra
if salary > 50000:
  it = (salary - 50000)*0.3
  netsal = salary - it
print("Name : ", name)
print("Basic Pay : ", basic)
print("DA : ", da)
print("HRA : ", hra)
print("Income Tax monthly : ", it)
print("Net Monthly Salary : ", netsal)
