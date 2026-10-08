# 4. Calculate the Average of Set Elements
# Write a Python program to create a set of integers and calculate the average of all elements.

s=set()
total=0
size=int(input("enter size"))

print("enter value")
for i in range(size):
    no=int(input())
    s.add(no)
    
for i in s:
    total=total+i
    avg=total/size
    
print(avg)
    