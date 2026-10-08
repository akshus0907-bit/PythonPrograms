


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
