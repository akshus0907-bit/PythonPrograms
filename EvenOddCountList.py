

size=int(input("enter size"))
number=[]

print("enter element ")
for i in range(size):
    no=int(input())
    number.append(no)
    
evencount=0
oddcount=0

for i in range(size):
    if number[i]%2==0:
        evencount+=1
        
print("even count",evencount)

for i in range(size):
    if number[i]%2!=0:
        oddcount+=1
        
print("odd count",oddcount)