# 8.Find the Difference Between Maximum and Minimum
# Write a Python program to create a set of integers and calculate the difference between the maximum and
# minimum elements.

s=set()

size=int(input("enter size"))
print("enter element")
for i in range(size):
    no=int(input())
    s.add(no)
    
m=min(s)
print(m)
m2=max(s)
print(m2-m)
    