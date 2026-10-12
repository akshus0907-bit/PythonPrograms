#Q8.Find the index of a given element in a tuple.


size=int(input("enter size"))

lst=[]

print("enter number")
for i in range(size):
    no=int(input())
    lst.append(no)
    
tup=tuple(lst)

num=int(input("enter number to find index "))
if num in tup:
    print("number found",tup.index(num))
    
else:
    print("number not found")
    
    
        