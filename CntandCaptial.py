# Q.7
# Display the dictionary.
# Country and Capital
# Write a Python program to take the names of three countries and their capitals from the user and store them in a dictionary. Display all country-capital pairs.

cntcap={}

value=int(input("enter number of input"))

for i in range(value):
    cnt=input("enter country name")
    cap=input("enter capital name")
    
    cntcap[cnt]=cap
  
print(cntcap)
