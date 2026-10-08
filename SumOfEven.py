# 5.Find the Sum of Even Numbers
# Write a Python program to create a set of integers and calculate the sum of only the even numbers.

s=set()
sum=0
size=int(input("enter size"))
print("enter value")
for i in range(size):
    no=int(input())
    s.add(no)
    
for i in s:
    if i%2==0:
        sum=sum+i
        
print(sum)