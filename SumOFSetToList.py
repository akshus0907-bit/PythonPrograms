# 7.Add Corresponding Elements from Two Sets
# Write a Python program to create two sets containing the same number of elements. Convert them into 
# lists and calculate the sum of corresponding elements.
# Sample Input:
# Set 1 = {10, 20, 30}
# Set 2 = {1, 2, 3}
# Sample Output:
# 11
# 22
# 33

s1=set()
s2=set()
size=int(input("enter the size is both set"))
print("enter value of first set")
for i in range(size):
    no=int(input())
    s1.add(no)
    
print("enter value of second set")    
for i in range(size):
    no2=int(input())
    s2.add(no2)
    



list1=list(s1)
list2=list(s2)
print("Corresponding sums:")
for i in range(size):
    result=list1[i]+list2[i]

    print(result)


