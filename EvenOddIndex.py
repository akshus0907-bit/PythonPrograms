


size=int(input("enter size"))
number=[]
print("enter element")
for i in range(size):
    no=int(input())
    number.append(no)
    
print("value  at even index") 
for i in range(size):
    if i%2==0:
        print(number[i])
        
print("value at odd index")      
for i in range(size):
    if i%2!=0:
        print(number[i])
        