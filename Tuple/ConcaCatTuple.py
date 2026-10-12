#Q10Concatenate two tuples.

size=int(input("enter size of first tuble"))

lst1=[]

print("enter number")
for i in range(size):
    no=int(input())
    lst1.append(no)
    
tup=tuple(lst1)
    
size=int(input("enter size of Second tuble"))

lst2=[]

print("enter number")
for i in range(size):
    no1=int(input())
    lst2.append(no1)
    
tup2=tuple(lst2)


tup3=tup+tup2

print(tup3)