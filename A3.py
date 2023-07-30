#write a python program to input time in seconds and convert to hours, minutes and seconds.

time = int (input("Enter time in seconds : "))
hours = time//3600
minutes = (time%3600)//60
seconds = (time%3600)%60
print("Hours = ", hours)
print("Minutes = ", minutes)
print("Seconds = ", seconds)
