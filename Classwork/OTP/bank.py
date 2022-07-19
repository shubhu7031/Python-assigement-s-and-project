def deposit(cr_bal,add_amt):
    return cr_bal + add_amt

def withdraw(cr_bal,remove_amt):
    if remove_amt > cr_bal:
        print(f"you can not withdraw more than {cr_bal}")
        return cr_bal
    else:
            cr_bal=cr_bal - remove_amt
            print("********************************")
            print("transaction successfull")
            print(f"your current balance is {cr_bal}")
            print("********************************")
            return cr_bal

            

def bank():
    
    current_bal=int(input("Enter the amount in order to open your account:"))
    print(f"Your account has been created successfull, your account balance is {current_bal}")


    keeplooping = True
    
    while keeplooping:

        print("Welcome to the Bank")
        print("Press 1 for the deposit")
        print("Press 2 for the withdraw")
        print("Press 3 for the checkblance")
        print("Press 4 for the exit")


        op=int(input("Enter your choice: "))

        if op==1:
            depo_bal=int(input("Enter your amount to deposit:"))
            print("********************************")
            current_bal=deposit(current_bal,depo_bal)
            print(f"Your balance is now {current_bal}")
            print("********************************")
            print("Your transaction is successfull")
        
        elif op==2:
            remove_amt=int(input("Enter your amount to withdraw:"))
            print("********************************")
            current_bal=withdraw(current_bal,remove_amt)
            print("********************************")

        elif op==3:
            print(f"Your current balance is {current_bal}")

        elif op==4:
            print("thank you for using bank")
            keeplooping=False
            break
        else:
            keeplooping=False
            break