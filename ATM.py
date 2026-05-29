balance=100
while True:
    print("======ATM Menu======")
    print("1. Check Balance")
    print("2.Deposit Money")
    print("3. Withdraw money")
    print("4. Exit")
    c=int(input("Enter your choice"))
    if(c==1):
        print("Your current balance is:",balance)
    elif(c==2):
        a=int(input("Enter the amount you want to deposit:"))
        balance=balance+a
        print("Your current balance is:",balance)
    elif(c==3):
        w=int(input("Enter the amount you want to withdraw:"))
        if(w>balance):
            print("Insufficient balnce")
        else:
            balance=balance-w
            print("Your current balance is:",balance)
    elif(c==4):
        print("Thank You!")
        break
    else:
        print("Invalid choice!")
