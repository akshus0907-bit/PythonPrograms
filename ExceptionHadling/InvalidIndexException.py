# Q3. List Index Error
# Create a list of five numbers. Ask the user to enter an index and display the corresponding element. Handle an invalid index.

lst=[10,20,30,40,50]

try:
    index=int(input("enter index to display element  "))
    print(lst[index])
    
except IndexError:
    print("invalid index")
    
