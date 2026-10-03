# Question 13: Write a java program to display only non-zero values from an array.
# Asked In Practice assignment
# Input : Array = {1, 0, 5, 0, 7, 0, 9}
# Output : Non-zero elements = {1, 5, 7, 9}
# Explanation :
# Traverse the array and print only elements that are not equal to zero.



size=int(input("enter size"))

number=[]
print("enter element")
for i in range(size):
    no=int(input())
    number.append(no)
    
    
for i in range(size):
    if(number[i]!=0):
        print(number[i],end="\t")
    
    