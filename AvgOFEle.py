

size=int(input("enter size"))
number=[]
print("enter element")

for i in range(size):
    no=int(input())
    number.append(no)
    
sum=0;
count=0;
for i in range(size):
    sum=sum+number[i]
    
    count=count+1
    
print(sum/count)
    
