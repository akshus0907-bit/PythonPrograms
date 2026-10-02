# Q6. Find the sum of numbers from 1 to 10.

# Expected:

# Sum = 55

sum=0
for i in range(1,11):
    sum=sum+i
print(sum)



# Q11. Take a number from the user and calculate the sum of its digits.

# Example:

# Enter number: 1234

# Expected:

# Sum = 10

# Because:

# 1 + 2 + 3 + 4 = 10
no=int(input("enter number "))
sum=0
while(no>0):
    digit=no%10
    sum=sum+digit
    no=no//10
    
print(sum)   


# Q13. Take a number from the user and check whether it is prime.

# Example:

# Enter number: 7

# Expected:

# Prime

# Hint:

# Check whether the number is divisible by any number from 2 to n-1.

no=int(input("enter number"))

flag =True
for i in range(2,no):
        if(no%i==0):
            
            flag=False
            break
            
if (flag==True):
    print("prime number")
       
else:
    print("not prime")    
            
            
            
            
         
    