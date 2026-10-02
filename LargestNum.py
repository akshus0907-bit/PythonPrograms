#Q4. Take three numbers from the user and print the largest number using an if-elif-else structure.

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if(a>b and a>c):
    print(a,"is largest")
  
elif(b>c):
    print(b,"is largest")
    
else:
    print(c,"is largest")
  