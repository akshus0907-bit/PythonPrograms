# Q5. Create a menu:
# 1. Addition
# 2. Subtraction
# 3. Exit

# Keep displaying the menu until the user selects 3.
a=int(input("enter number"))
b=int(input("enter number"))
while True:
    print("1.Addition \n2.Subtraction \n3.Exit")
    
    choice=int(input("enter choise 1-3"))
    
    if choice==1:
        print("Addition:",a+b)
        
    elif choice==2:
        print("Subtraction:",a-b)

    elif choice==3:
        print("Exit")
        break 

    else:
        print("invalid choicce")
        
        