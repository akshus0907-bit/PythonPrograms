
# 10.Find Common Even Numbers

# Write a Python program to create two sets and display the common elements that are even numbers.
# Sample Input:
# Set 1 = {2, 3, 4, 5, 12, 35}
# Set 2 = {1,2,5,4,6,12}
# Sample Output:
# 2
# 4
# 12

s1=set()
s2=set()

size=int(input("enter size"))
print("enter value in first set")
for i in range(size):
    no=int(input())
    s1.add(no)
print("enter value in secong set")
for i in range(size):
    no2=int(input())
    s2.add(no2)
    
for i in s1:
    if i in s2 and i%2==0:
        print(i)
        
   