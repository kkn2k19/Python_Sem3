#A company wants to set target for each of the four regions (EAST, WEST, NORTH and SOUTH). The company allots the following percentage target for each region.
# East   15%
# West   25%
# North  30%
# South  30%
#write a program to input total target and print out the breakup of the target for each region.

total = float(input("Enter total target : "))
east = total*0.15
west = total*0.25
north = total*0.3
south = total*0.3
print("East : ", east)
print("West : ", west)
print("North : ", north)
print("South : ", south)
