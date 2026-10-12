#Q9. Check if an element exists in a tuple.


size=int(input("enter size"))
lst=[]
print("enter number ")
for i in range(size):
    no=int(input())
    lst.append(no)
    
tup=tuple(lst)
num=int(input("enter number to check in tuble "))

if num in tup:
    print("number is exists in tuple")
   
else:
    print("number is not exists in tuple")