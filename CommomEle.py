

size=int(input("enter size"))
number=[]
print("enter element")
for i in range(size):
     no=int(input())
     number.append(no)
     
     

size1=int(input("enter size"))
number1=[]
print("enter element")
for i in range(size1):
     n=int(input())
     number1.append(n)
     
     
     
for i in range(size1):
    for j in range(size1):
        if number[i]==number1[j]:
            print(number[i],end="\t")
            break
     
     
