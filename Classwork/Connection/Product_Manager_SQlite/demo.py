import sqlite3
import tabulate

con=sqlite3.connect('productmanager.db')

mydb=con.cursor()

def login():
    login.login_id=input("Enter your login ID: ")
    login.password=input("Enter your password: ")

    mydb.execute("SELECT *FROM login WHERE login_id=:login AND password=:password",{"login":login.login_id,"password":login.password})
    if mydb.fetchone():
        print("successfully")
        mydb.execute("SELECT Role FROM login WHERE login_id=:login AND password=:password",{"login":login.login_id,"password":login.password})
        role=mydb.fetchone()
        role=role[0]
        if role=="admin":
            print("you are admin")
        else:
            print("you are customer")
    else:
        print("error")
    

def register():
    register.login_id=input("register your login ID:")
    register.Role=input("Specify your role:")
    register.password=input("create your password:")
    c_password=input("Confirm your password:")
    if register.password==c_password:
        mydb.execute("insert into login values(?,?,?)",(register.login_id,register.password,register.Role))
        if mydb.rowcount==1:
            print("data successfully inserted")
            con.commit()
        else:
            print("something went wrong!!!")

def userside():
    count=1
    menu_list=["Add item","remove item","View item","checkout","exit"]
    for i in menu_list:
        print(f"{count} {i}")
        count+=1

    user_choice=int(input("Enter your choice:"))
    
    if user_choice==1:
        print("Add item")
    elif user_choice==2:
        print("remove item")
    elif user_choice==3:
        print("view item")
    elif user_choice==4:
        print("checkout")
    else:
        print("exit")


def add_item_admin():
    product_name=input("Enter name of the product:")
    product_quantity=int(input(f"Enter quantity of {product_name}:"))
    product_price=int(input(f"Enter price of the {product_name} per head:"))
    mydb.execute("select * from details WHERE productname=:product",{"product":product_name})
    if mydb.fetchone():
        print("data already exists")
    else:
        mydb.execute("insert into details values(?,?,?)",(product_name,product_quantity,product_price))
        mydb.execute("select * from details where productname=:product AND Quantity=:quantity AND price=:price",{"product":product_name, "quantity":product_quantity,"price":product_price})
        if mydb.fetchone():
            print("data enter successfully!!!")
            con.commit()
        else:
            print("data not successfully inserted!!!")
            con.rollback()

def remove_item_admin():
    product_name=input("Enter the name of the product to remove:")
    product_quantity=input("Enter the quantity of the product:")

    mydb.execute("select * from details WHERE productname=:product",{"product":product_name})
    if mydb.fetchone():
        data=mydb.fetchone()
        print(data)
        print(tabulate.tabulate(data,headers=["product_name","quantity","Price"]))
    else:
        print("no data found")


remove_item_admin()
