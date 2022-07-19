import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="topsapp")
db=con.cursor()

def main():

    main.fname=input("Enter your first name:")
    main.lname=input("Enter your last name:")
    main.gender=input("Enter your gender:")
    main.age=input("Enter your age:")

def create():
    main()
    query="insert into Metadata (Fname,lname,age,gender) values('%s','%s','%s','%s')"
    args=(main.fname,main.lname,main.age,main.gender)
    data=db.execute(query%args)
    if data:
        print("recored successfully inserted!!!")
    else:
        print("something went wrong!!!!")
    con.commit()
def read():
    name=input("Enter your first name to search:")
    query="select * from Metadata WHERE Fname='%s'"
    args=(name)
    data=db.execute(query%args)
    if data:
        fetch=db.fetchone()
        # id=fetch[0]
        # fname=fetch[1]
        # lname=fetch[2]
        # gender=fetch[3]
        # age=fetch[4]

        print(f"your ID:{fetch[0]}\nyour fname :{fetch[1]}\nyour lname:{fetch[2]}\nyour gender:{fetch[3]}\nyour age:{fetch[4]}")
    else:
        print("something went wrong!!!!")
    con.commit()

def update():
    main()
    print("----------------update---------------")
    fname=input("Enter your update first name:")
    lname=input("Enter your update last name:")
    gender=input("Enter your gender:")
    age=input("Enter your age:")
    query ="update Metadata SET Fname='%s',lname='%s',gender='%s',age='%s' WHERE Fname='%s' AND lname='%s'"
    args=(fname,lname,gender,age,main.fname,main.lname)
    data=db.execute(query%args)
    if data:
        print("-------------------")
        print("recored successfully update!!!")
        print("-------------------")
    else:
        print("-------------------")
        print("somrthing went wrong!!!")
        print("-------------------")
    con.commit()

def delete():
    f_name=input("Enter your fname:")
    l_name=input("Enter your lname:")
    query="delete from Metadata WHERE Fname='%s' AND lname='%s'"
    args=(f_name,l_name)
    data=db.execute(query%args)
    if data:
        print("-------------------")
        print("recored successfully delete!!!")
        print("-------------------")
    else:
        print("-------------------")
        print("somwthing went wrong!!")
        print("-------------------")
    con.commit()

while True:
    print("------------------------------------------------")
    print("press 1 : create recored")
    print("press 2: read recored")
    print("press 3: update recored")
    print("press 4: Delete recored")
    print("press 5: for exit")
    print("------------------------------------------------")

    user_choice=int(input("Enter your choice:"))

    if user_choice==1:
        create()
    elif user_choice==2:
        read()
    elif user_choice==3:
        update()
    elif user_choice==4:
        delete()
    elif user_choice==5:
        break
    else:
        print("wrong choice!!")
