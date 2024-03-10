#Write a program to remove the given key from a dictionary
#  railfall = {'SUNDAY':3.4, 'MONDAY':5.6, 'TUESDAY':4.2, 'WEDNESDAY':1.0, 'THURSDAY':0.0, 'FRIDAY':2.5, 'SATURDAY':3.1}

railfall = {"SUNDAY": 34, "MONDAY": 5.6, "TUESDAY": 4.2, "WEDNESDAY": 1.0, "THURSDAY": 0.0, "FRIDAY": 2.5, "SATURDAY": 3.1}
key_to_remove = input("Enter the key to remove: ")
railfall.pop(key_to_remove, None)
print("Updated Dictionary:", railfall)
