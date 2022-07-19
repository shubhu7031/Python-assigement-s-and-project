class bank:

    current_balance=0
    deposit_balance=0
    withdraw_balance=0


    def __init__(self):
        self.name=input("Enter your name:")
        self.number=int(input("Enter your number:"))
        print(f"Welcome {self.name}!!")

    def deposit(self):
        
        self.deposit_balance=int(input("Enter the amount you want to deposit:"))

        if self.deposit_balance<0:
            print("you can't depoist the amount below 1")
            print("kindly check the amount")
            self.deposit()
        else:
            self.current_balance=self.current_balance+self.deposit_balance
            print("your amount is successfully deposit")
            print(f"your current balance is {self.current_balance}")


    
    def withdraw(self):

        self.withdraw_balance=int(input("Enter the amount to withdraw:"))

        if self.withdraw_balance>self.current_balance:
            print("you don't have enough funds to withdraw")
            print(f"your available balance is is {self.current_balance}")
        
        else:
            self.current_balance=self.current_balance-self.withdraw_balance
            print(f"your request for withdraw balance:{self.withdraw_balance}")
            print("your withdraw request is successfully completed")
            print(f"available balance is {self.current_balance}")
    
    def display_balance(self):
        print(f"your available balance is {self.current_balance}")




print("Welcome to apni bank")
obj=bank()
print(""" 
press 1: for deposit
press 2: for withdrawal
press 3: for check balance
press 4:for exit""")

keeplooping="TRUE"

while keeplooping:

    user_option=int(input("please select the option:"))

    if user_option==1:
        print("deposit section")
        obj.deposit()
    elif user_option==2:
        print("withdrawal section")
        obj.withdraw()
    elif user_option==3:
        obj.display_balance()
    elif user_option==4:
        print("Exit")
        keeplooping=="FALSE"
        break
    else:
        print("invalid option")


