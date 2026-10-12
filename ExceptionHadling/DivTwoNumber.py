# Q1. Division of Two Numbers
# Write a Python program to divide two numbers. Handle the exception that occurs when the denominator is zero.


a=int(input("enter first number"))
b=int(input("enter second number"))

try:
    div=a/b
    print(div)
    
except ZeroDivisionError:
    print("number cannot divided by zero")