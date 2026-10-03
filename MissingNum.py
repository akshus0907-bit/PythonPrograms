

size=int(input("enter size:"))

number=[]

print("enter element:")
for i in range (size):
    no=int(input())
    number.append(no)

min=number[0]
max=number[0]

for i in range(1,len(number)):
    if(number[i]<min):
        min=number[i]
        
        
    if(number[i]>max):
        max=number[i]
        
        
for i in range(min,max):
    if i not in number:
        print("missing number is :",i)
    