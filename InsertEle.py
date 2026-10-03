


size=int(input("enter size"))

number=[]
print("enter element")
for i in range(size):
    no=int(input())
    number.append(no)
    
number.append(0)

ele=int(input("enter element to insert"))
position=int(input("enter position to insert elemente"))


for i in range(size,position,-1):
    number[i]=number[i-1]
    
number[position]=ele
    
print("element ")
for i in range(size):
    print(number[i])
    