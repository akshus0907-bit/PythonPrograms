# Q.Create a function that returns the sum of digits of a number.

# Use % and //.

# Input: 1234
# Output: 10

def  sumofDigit(no):
    sum=0;

    
    while(no>0):
        digit=no%10
        sum=sum+digit
        no=no//10
 
    return sum
    
no=int(input("enter number "))
result=sumofDigit(no)
print(result)
    
    
    
# countDigits(no)

# Create a function that returns the number of digits.

# Input: 12345
# Output: 5

def countDigits(num):
    count=0

    while(num>0):
        count=count+1
        num=num//10
    return count
    
    
num=int(input("enter number"))
result=countDigits(num)
print(result)