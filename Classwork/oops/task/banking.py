#Parent class :User #done
#has function to show user details #done
#Child class : Bank #done
# store details like account number, account balance #done 
#allow the user deposit withdraw and check balance #done 

class User:
    def __init__(self,name,info,age,PAN):
        self.name = name
        self.info = info
        self.age = age
        self.PAN = PAN

    def detail(self):
        print(f"name:{self.name}\n details:{self.info}\n age:{self.age}\n PANCARD:{self.PAN}")

obj=User("Shubham","nahi kevi","21","AVB1209PC")

obj.detail()


class Bank(User):
    def __init__(self,account_number,account_balance):
        self.account_number = account_number
        self.account_balance = account_balance
        print(f"account_balance:{account_balance}")
        print(f"account_number:{account_number}")
    


    def deposit(self,account_balance,add_amt):
        self.account_balance = account_balance
        self.add_amt = add_amt

        print(f" balance after depoist:{account_balance + add_amt}")




    def withdraw(self,remove_amt,account_balance):
        self.remove_amt = remove_amt
        self.account_balance = account_balance
        if remove_amt > account_balance:
            print(f"you can not withdraw more than {account_balance}")
            return account_balance
        else:
            account_balance =account_balance - remove_amt
            print("********************************")
            print("transaction successfull")
            print(f"your current balance is {account_balance}")
            print("********************************")
            return account_balance
    
        

d1=Bank(123456789,100)
d1.deposit(100,100)
d1.withdraw(100,10000)