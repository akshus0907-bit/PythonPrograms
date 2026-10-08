# Q.9
# Subject Marks
# Write a Python program to take subject names and marks for three subjects and store them in a dictionary
# Display all subjects and marks and calculate the average marks.

submark={}

val=int(input("enter number of input"))
for i in range(val):
    subject=input("enter subject name")
    marks=int(input("enter marks"))
    
    submark[subject] = marks

print(submark)

total=0;
for key,value in submark.items():
    print(key , ":" , value)
    total=total+value
avg=total/val
print(avg)