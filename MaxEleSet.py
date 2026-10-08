# 2.Find the Maximum Element
# Write a Python program to create a set of integers and find the largest element in the set.

s=set()

size=int(input("enter size"))
max=0
print("enter value")
for i in range(size):
    no=int(input())
    s.add(no)
    
    
    if(no>0):
        max=no
print(max)
    
    
