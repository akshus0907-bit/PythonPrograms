# Q1. Day Menu

# Take a number from the user and print:

# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# 4 → Thursday
# 5 → Friday
# 6 → Saturday
# 7 → Sunday

# Use match-case.

day=int(input("enter number from 1 to 7"))

match day :
    case 1:
        print("Monday")
        
    case 2:
        print("tuesday")
        
    case 3:
        print("wednesday")
        
    case 4:
        print("thusday")
        
    case 5:
        print("friday")
        
    case 6:
        print("saturday")
  
    case 7:
        print("sunday")
      
    case_:
        print("invalid choice")    
        
        
        

