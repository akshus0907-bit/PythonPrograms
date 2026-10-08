#fun with unppacking

def get_users():
    return 10,20,30,40
a,*b=get_users()
print(a,"\n ",b)