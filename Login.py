# Q.8
# Simple Login System
# Write a Python program to create a ictionary containing usernames and passwords. 
# Ask the user to enter a username and password and check whether the login details are correct.

login={}

username='aksh'
password='123'

login["username"]=username
login["password"]=password

uname=input("enter username:")
upass=input("enter username:")

if(login["username"]==uname and login["password"]==upass):
    print("correct")
    
else:
    print("invalid")
