# Q.3
# Phone Book
# Write a Python program to take a person's name and phone number as input and store them in a dictionary.
# Ask the user for a name and display the corresponding phone number.

phoneBook={}

name=input("enter name")

phone=input("enter phone number")

phoneBook[name]=phone

search=input("enter name")

if search in phoneBook:
    print(phoneBook[search])
    
else:
    print("not  found")
