# 3. Find the Minimum Element
# Write a Python program to create a set of integers and find the smallest element in the set.

s=set()

size=int(input("enter size"))

print("enter value")
for i in range(size):
    no=int(input())
    s.add(no)
    

minimum=min(s)
print(minimum)
