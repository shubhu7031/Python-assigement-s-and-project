# import pymysql
# from soupsieve import select

# con=pymysql.connect(host="localhost",user="root",password="",database="topsapp")
# db=con.cursor()

# def deposit(cr_bal,add_amt):
#     cr_bal=cr_bal+add_amt
#     query="insert into bank (current_bal) values('%s')"
#     args=(cr_bal)
#     data=db.execute(query%args)
#     if data:
#         print("success")
#     else:
#         print("something went wrong!!!")
#         print("Please try again!!!")
#     return cr_bal + add_amt

# def withdraw(cr_bal,remove_amt):
#     if remove_amt > cr_bal:
#         print(f"you can not withdraw more than {cr_bal}")
#         return cr_bal
#     else:
#             cr_bal=cr_bal - remove_amt
#             print("********************************")
#             print("transaction successfull")
#             print(f"your current balance is {cr_bal}")
#             print("********************************")
#             return cr_bal

            




# def bank():
#     name=input("Enter your name:")
#     age=input("Enter your age:")
#     gender =input("Enter your gender:")
#     current_bal=int(input("Enter the amount in order to open your account:"))

#     query ="insert into bank (name, age, gender,current_bal) values ('%s','%s','%s','%s')"
#     args=(name,age,gender,current_bal)
#     data=db.execute(query%args)
#     select_query="select * from bank WHERE name='%s'"
#     args=(name)
#     data=db.execute(select_query%args)
#     one=db.fetchone()
#     if data:

#         print(f"Your account has been created successfull, your account balance is {current_bal}")
#         print(f"Your id is {one[0]}")
#     else:
#         print("try again!!")


#     keeplooping = True
    
#     while keeplooping:

#         print("Welcome to the Bank")
#         print("Press 1 for the deposit")
#         print("Press 2 for the withdraw")
#         print("Press 3 for the checkblance")
#         print("Press 4 for the exit")


#         op=int(input("Enter your choice: "))

#         if op==1:
#             depo_bal=int(input("Enter your amount to deposit:"))
#             print("********************************")
#             current_bal=deposit(current_bal,depo_bal)
#             print(f"Your balance is now {current_bal}")
#             print("********************************")
#             print("Your transaction is successfull")
        
#         elif op==2:
#             remove_amt=int(input("Enter your amount to withdraw:"))
#             print("********************************")
#             current_bal=withdraw(current_bal,remove_amt)
#             print("********************************")
#             query="UPDATE bank SET current_bal='%s' WHERE name='%s'"
#             args=(current_bal,name)
#             data=db.execute(query,args)
#             if data:
#                 print("successfull")
#             else:
#                 print("error")

#         elif op==3:
#             print(f"Your current balance is {current_bal}")

#         else:
#             keeplooping=False
#             break


# bank()


def fun1():
    fun1.var="hello"

def fun2():
    print(fun1.var)

fun1()
fun2()
