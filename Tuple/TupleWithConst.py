#tuple with constant

ALLOWE_ROLE=(
    "developer"
    "admin"
    "manager"
    )
    
role=input("enter role")

if role in ALLOWE_ROLE:
    print("valid role")
    
else:
    print("not allowed role")