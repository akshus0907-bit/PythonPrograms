# Q. printTable(no)

# Create a function that prints the multiplication table of a number from 1 to 10.

def table(no):
    for i in range(1,11):
        print(no*i)

no=int(input("enter number"))

table(no)    
        