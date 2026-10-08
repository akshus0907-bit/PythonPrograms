# 6.Find the Square of Each Element
#  Write a Python program to create a set of integers and create a new set containing the square of each
# element.

s=set()

size=int(input("enter size"))
for i in range(size):
    no=int(input())
    s.add(no)
    
sqt=set()

for i in s:
    square=i*i
    sqt.add(square)
print(s)
print(sqt)

