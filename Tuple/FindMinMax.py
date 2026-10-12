#Q18.Find the maximum and minimum


size=int(input("enter size"))

lst=[]
print("print number")
for i in range(size):
    no=int(input())
    lst.append(no)
  
  
tup=tuple(lst)
maximum=tup[0];
minimum=tup[0]

for i in range(size):
    if tup[i]>maximum:
        maximum=tup[i];
    if tup[i]<minimum:
        minimum=tup[i]
        

print("max:",maximum)
print("min",minimum)
