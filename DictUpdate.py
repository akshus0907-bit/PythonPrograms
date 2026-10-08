# Q.5
# Dictionary Update
# Write a Python program to create a dictionary containing three key-value pairs. 
# Ask the user for a key and a new value, then update the dictionary with the new value. 
# Display the updated dictionary.

dict={"name":"Akshata",
       "age":23,
       "marks":87
      }
      
print("dict before update")   
print(dict)

key=input("enter key for update")
val=input("enter value for update")

dict[key]=val

print("dict after update",dict)


