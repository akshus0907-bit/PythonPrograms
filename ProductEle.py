# 9.Find the Product of All Elements
# Write a Python program to create a set of integers and calculate the product of all elements.

pro=1
s=set()
size=int(input("enter size"))
for i in range(size):
    no=int(input())
    s.add(no)
    
for i in s:
    pro=pro*i
print(pro)
