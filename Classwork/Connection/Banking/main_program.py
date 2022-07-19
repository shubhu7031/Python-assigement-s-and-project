import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="bank")
db=con.cursor()



def user_login():

    user_login.login_id=input("Enter your login id:")
    user_login.password=input("Enter your password:")

    query ="select * from bank where login_id='%s' AND password='%s'"
    args=(user_login.login_id, user_login.password)
    data=db.execute(query%args)
    if data:
        data_tuple=db.fetchone()
        user_login.current_bal=data_tuple[4]
        print(f"your current balance is {user_login.current_bal}")
        con.commit()
    else:
        print("something went wrong")   

def register():
    name=input("Enter your name:")
    age=input("Enter your age:")
    gender=input("Enter your gender:")
    balance=input("Enter the minimum balance to open account:")
    print("----------------------------------------------------------")
    login_id=input("Enter your login_id:")
    password=input("create your password:")
    c_password=input("conform your password:")
    if password==c_password:

        query ="insert into bank (name, age, gender,current_bal,login_id,password) values('%s','%s','%s','%s','%s','%s')"
        args=(name, age, gender, balance,login_id, password)
        data=db.execute(query%args)
        if data:
            print("account successfully created")
        else:
            print("something went wrong")
    con.commit()

def deposit(deposit_bal):

    user_login.current_bal=user_login.current_bal+deposit_bal
    query="update bank set current_bal='%s' WHERE login_id='%s'"
    args=(user_login.current_bal,user_login.login_id)
    data=db.execute(query%args)
    if data:
        print("Amount successfully Added!!!")
        print(f"you have {user_login.current_bal} in your account")
    else:
        print("Something went wrong!!")
    con.commit()


def withdraw_balance(withdraw_amount):
    
        if withdraw_amount>user_login.current_bal:
            print("you don't have insufficient funds to withdraw:")
            print(f"available fund is {user_login.current_bal}")
        else:
            user_login.current_bal=user_login.current_bal-withdraw_amount
            print(user_login.current_bal)
            query = "update bank SET current_bal='%s' WHERE login_id='%s'"
            args=(user_login.current_bal,user_login.login_id)
            print(user_login.current_bal)
            data=db.execute(query%args)
            if data:
                print("Amount successfully withdraw:")
                print(f"You have {user_login.current_bal} in your account")
                con.commit()
                
            else:
                print("Something Went wrong!!")
        con.commit()


def show_balance():
    query="select * from bank WHERE login_id='%s'"
    args=(user_login.login_id)
    data=db.execute(query%args)
    if data:

        data_tuple=db.fetchone()
        id=data_tuple[0]
        name=data_tuple[1]
        gender=data_tuple[2]
        age=data_tuple[3]
        current_bal=data_tuple[4]
        print(f"your id :{id}\nyour name:{name}\nyour gender:{gender}\nyour age:{age}\nyour current bal:{current_bal}")
    else:
        print("something went wrong")
        show_balance()

def bank():
    query="select * from bank WHERE login_id='%s'"
    args=(user_login.login_id)
    data=db.execute(query%args)
    if data:

        data_tuple=db.fetchone()
        current_bal=data_tuple[4]
    else:
        print("something went wrong")
        
    
    while True:

        print("-------------------------------------------")
        print("Welcome to the Bank")
        print("Press 1 for the deposit")
        print("Press 2 for the withdraw")
        print("Press 3 for the checkblance")
        print("Press 4 for the exit")
        print("--------------------------------------------")


        print("---------------------------------------------")
        op=int(input("Enter your choice to continue:"))

        if op==1:
            deposit_amt=int(input("Enter the deposit amount:"))
            deposit(deposit_amt)
        elif op==2:
            withdraw_amount=int(input("Enter the withdraw amount:"))
            withdraw_balance(withdraw_amount)
        elif op==3:
            show_balance()
        else:
            break
    con.commit()

def main():
    print("press 1 : for new user:")
    print("press 2 : for already existing user:")
    user_choice=int(input("Enter your choice: "))

    if user_choice==1:
        register()
        bank()
    elif user_choice==2:
        user_login()
        bank()
    else:
        print("something went wrong:")


main()