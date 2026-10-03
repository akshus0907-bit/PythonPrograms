



size=int(input("enter size of list"))
number=[]
num=[0]*size


print("enter element")
for i in range(size):
    no=int(input())
    number.append(no)
    
for i in range(size):
      num[i]=number[i]
       
print(num)