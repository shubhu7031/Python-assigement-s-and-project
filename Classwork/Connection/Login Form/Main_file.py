import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="topsapp")
db=con.cursor()




def insert():

    user_id=input("Enter your userid:")
    password=input("Enter your password:")

    query="insert into details (login_id,password) values ('%s','%s')"
    args=(user_id,password)

    data=db.execute(query%args)
    if data:
        print("successfully registered")
    else:
        print("something went wrong")

    con.commit()

def search():
    
    user_id=input("Enter your userid:")
    password=input("Enter your password:")

    query="select * from details WHERE login_id='%s' AND password='%s'"
    args=(user_id,password)

    data=db.execute(query%args)
  
    if data:
        print("your are successfully login")
    else:
        print("please try again!!!")

    con.commit()

def main():

    print("press 1 : for registration:")
    print("press 2 : for login:")
    print("press 3 for exit:")

user_input=int(input("Enter your choice:"))
        


while True:

    if user_input==1:
        insert()
        main()
        user_input=int(input("Enter your choice:"))
    elif user_input==2:
        search()
        main()
        user_input=int(input("Enter your choice:"))
    elif user_input==3:
        break
    else:
        print("try again::")
        main()
        user_input=int(input("Enter your choice:"))
        