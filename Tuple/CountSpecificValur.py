#Q7.Count how many times a specific value appears in a tuple.

size=int(input("enter size of tuple"))

lis=[]
print("enter number")
for i in range(size):
    no=int(input())
    lis.append(no)
tup=tuple(lis)	
	
num=int(input("enter number to count"))
count=0
for i in range(size):
	if tup[i]==num:
		count=count+1
print(count)
		

