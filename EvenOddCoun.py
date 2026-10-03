

size=int(input("enter size"))
number=[]

for i in range(size):
    no=int(input())
    number.append(no)
   
count=0   
for i in range(size):
    if(number[i]%2==0):
        count=count+1
print("count of even values",count)

print()

count=0
for i in range(size):
    if(number[i]%2!=0):
        count=count+1
print("count of odd index",count)
    

