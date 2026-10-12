#Q12.Convert a list into a tuple

size=int(input("enter size"))
lst=[]
print("enter number")
for i in range(size):
    no=int(input())
    lst.append(no)
    
tup=tuple(lst)

print(tup)