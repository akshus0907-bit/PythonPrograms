#reverse number 


no=int(input("enter number"))

rev=0;
while no>0:
    digit=no%10
    rev=rev*10+digit
    no=no//10
    
    
print(rev) 
#-----------------------------------------------------------------------

no=int(input("enter number"))

rev=0;
for i in range(len(str(no))):
    digit=no%10;
    rev=rev*10+digit
    no=no//10
    
    
print(rev) 
