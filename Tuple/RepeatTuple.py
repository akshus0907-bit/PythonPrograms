#Q11.Repeat a tuple 3 times.

size=int(input("enter size"))

lst=[]

for i in range(size):
    no=int(input())
    lst.append(no)
    
tup=tuple(lst)
result=tup*3

print("origin tuple",tup)
print("tuple repeat three time",result)