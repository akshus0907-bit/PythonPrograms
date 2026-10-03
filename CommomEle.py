# Question 15: Write a java program to find common elements between two arrays.
# Asked In Practice assignment
# Input :
# Array1 = {1, 2, 3, 4, 5}
# Array2 = {3, 4, 5, 6, 7}
# Output : Common elements = {3, 4, 5}
# Explanation :
# Compare each element of Array1 with all elements of Array2, if match found ? it is a common element.

size=int(input("enter size"))
number=[]
print("enter element")
for i in range(size):
     no=int(input())
     number.append(no)
     
     

size1=int(input("enter size"))
number1=[]
print("enter element")
for i in range(size1):
     n=int(input())
     number1.append(n)
     
     
     
for i in range(size1):
    for j in range(size1):
        if number[i]==number1[j]:
            print(number[i],end="\t")
            break
     
     
