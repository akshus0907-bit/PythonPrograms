# Question 10: Write a program in java to delete an element at desired position from an array.
# Asked In Practice assignment
# Input the size of array : 5

# Input 5 elements in the array in ascending order :
# 1 2 3 4 5

# Input the position where to delete : 3

# Expected Output : The new list is : 1 2 3 5


size=int(input("enter size"))

number=[]
print("enter element")
for i in range(size):
    no=int(input())
    number.append(no)
    
position=int(input("enter position to delete number"))


index=position-1
for i in range(index,size-1):
    number[i]=number[i+1]
    
print("new list")
for i in range(size-1):
    print(number[i])
