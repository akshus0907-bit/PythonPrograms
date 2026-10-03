

size=int(input("enter size:"))
number=[]

print("enter element :")
for i in range(size):
    no=int(input())
    number.append(no)
    
    
L=0
R=len(number)-1
while(L<R):
    temp=number[L]
    number[L]=number[R]
    number[R]=temp
    L+=1
    R-=1
print(number)