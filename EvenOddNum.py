

size=int(input("enter size"))

number=[]

print("enter number")
for i in range(size):
    no=int(input())
    
    number.append(no)
    


print("even value",end=" ")
for i in range(size):
    
    if number[i]%2==0:
        print(number[i])
        



print("odd values",end="")
for i in range(size):
    if number[i]%2!=0:
        print(number[i])

        