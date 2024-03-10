#1.Write a program to input two lists from user and form a dictionary using its elements as key and values.

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()
dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)
