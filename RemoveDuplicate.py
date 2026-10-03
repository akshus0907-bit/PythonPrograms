

size=int(input("enter size"))
number=[]
print("enter element")
for i in range(size):
    no=int(input())
    number.append(no)
    
unique=[]

for i in range(size):
    duplicated=False
    for j in range(len(unique)):
        
        if number[i]==unique[j]:
            duplicated=True
            break
            
            
    if duplicated==False:
        unique.append(number[i])
        
for i in range(len(unique)):
    print(unique[i],end="\t")

        
