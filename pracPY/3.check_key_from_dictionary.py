#3. Python Program to check if a given key exists in a Dictionary or Not if present print its value in the dictionary.
#   railfall = {'SUNDAY':3.4, 'MONDAY':5.6, 'TUESDAY':4.2, 'WEDNESDAY':1.0, 'THURSDAY':0.0, 'FRIDAY':2.5, 'SATURDAY':3.1}

railfall = {'SUNDAY': 3.4, 'MONDAY': 5.6, 'TUESDAY': 4.2, 'WEDNESDAY': 10, 'THURSDAY': 0.0, 'FRIDAY': 2.5, 'SATURDAY': 3.1}
key_to_check = input("Enter the key to check: ")
if key_to_check in railfall:
    print("Value for", key_to_check + ":", railfall[key_to_check])
else:
    print("Key not found in dictionary")
