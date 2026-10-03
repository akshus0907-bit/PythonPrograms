# Question 11: Write a java program to give an array, find the second largest element.
# Asked In Practice assignment
# Input : Array = {12, 35, 1, 10, 34, 1}
# Output : Second largest = 34
# Explanation:
# First largest is 35, second largest is the next maximum (34). We maintain two variables (largest, secondLargest).

size=int(input("enter size"))
number=[]

print("enter number")

for i in range(size):
    no=int(input())
    number.append(no)
    
Max=number[0]
SecondMax=number[0]
for i in range(size):
    if number[i]>Max:
        SecondMax=Max
        Max=number[i]
        
    elif number[i]>SecondMax and number[i]!=max:
        secondMax=number[i]
print("max is :",Max)
print("second max is :",SecondMax)
    


