balance=10000
withdraw=int(input("enter withdrawl amount"))

if(withdraw<balance):
    print("withdrawal successful")
    balance=balance-withdraw
    print("reming balace is",balance)

else:
    print("Insufficient balance")