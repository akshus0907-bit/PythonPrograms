# Q14. Create a function getFactorial(no) that returns the factorial of a number.

# Example:

# Input: 5
# Output: 120
def getFactorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact

no=int(input("enter number"))
result=getFactorial(no)
print(result)    