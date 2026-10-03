# Question 2: Write a Java program to calculate the sum of all elements in an array.
# Asked In Practice assignment
# Input:
# Array Size = 5
# Array Elements = 2 4 6 8 10
# Output:



size=int(input("enter size:"))

number=[]
print("enter number:")
for i in range(size):
    no=int(input())
    number.append(no)
sum=0 
for i in range(size):
    sum=sum+number[i]
print("sum is :",sum)
    
    