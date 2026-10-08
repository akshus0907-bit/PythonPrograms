# Q.6
# Student Grade Dictionary
# Write a Python program to take a student's name and percentage as input. Store the student's name and 
# grade in a dictionary based on the following criteria:
# 75 and above → A
# 60 to 74     → B
# 40 to 59     → C
# Below 40     → Fail

student={}

name=input("enter name:")
per=int(input("enter persentage :"))


if(per>75):
    grade='A'
    
elif(per>74 and per<60):
    grade='B'
    
elif(per>59 and per<40):
    grade='C'
    
    
else:
    grade='fail'
   
studetn["name"]=name 
studetn["grade"]=grade  
print("name:",name)
print("grade:",grade)

