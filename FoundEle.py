


size=int(input("enter size"))
number=[]

for i in range(size):
    no=int(input())
    number.append(no)
    
search=int(input("enter number for search"))
for i in range(size):
    if number[i]==search:
        print("element", search,"found at index",i)