
size=int(input("enter size of list:"))

number=[]
print("enter number :")
for i in range(size):
    no=int(input())
    number.append(no)
    
print("list element")

for i in number:
    print(i,end='\t')
    
    