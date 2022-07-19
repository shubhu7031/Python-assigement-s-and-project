import pymysql
from tabulate import tabulate
from random import randint
import sqlite3

con=sqlite3.connect('productmanager.db')

mydb=con.cursor()



def login():
    login.login_id=input("Enter your login_id:")
    login.password=input("Enter your password:")
    query="SELECT * FROM login WHERE login_id=:login AND password=:passs"
    args=(login.login_id,login.password)
    data=mydb.execute(query%args)
    if data:
        print("Login successful")
        data_tuple=mydb.fetchone()
        role=data_tuple[2]
        print(role)
        if role=="admin":
            pass
        else:
            pass
    else:
        print("wrong credentials")

def register():
    login_id=input("regist your login_id:")
    password=input("create your password:")
    role=input("identify your role:")
    query="insert into login (login_id, password, role) values ('%s','%s','%s')"
    args=(login_id, password, role)
    data=mydb.execute(query%args)
    
    if data:
        print("account successfully created:")
        con.commit()
    else:
        print("something went wrong")

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

def remove_item_admin():
        print("Welcome to the remove item Section!")
        product_name=input("Enter name of the product:")
        query="select * from details WHERE Product_name='%s'"
        args=(product_name)
        data=mydb.execute(query%args)
        con.commit()
        if data:
            data=mydb.fetchone()
            Quantity=data[1]
            print(type(Quantity))
            user_choice=int(input(f"how many {product_name} you want to remove:"))
            if user_choice>Quantity:
                print(f"you can not remove more than {Quantity} {product_name}")
            else:
                Quantity=Quantity-user_choice
                query="update details SET Quantity='%s' WHERE Product_name='%s'"
                args=(Quantity,product_name)
                data=mydb.execute(query%args)
                con.commit()
                if data:
                    print("Item successfully Updated")
                else:
                    print("something went wrong")
                query="Select * from details WHERE Product_name='%s'"
                args=(product_name)
                data=mydb.execute(query%args)
                if data:
                    mydata=mydb.fetchone()
                    if mydata[1]==0:
                        query="delete from details WHERE product_name='%s'"
                        args=(product_name)
                        data=mydb.execute(query%args)
                        if data:
                            con.commit()
                else:
                    print("error")

def add_item_admin():
        print("Welcome to the Add item Section!")
        product_name=input("Enter the name of the product:")
        quantity=int(input(f"Enter the quantity of {product_name}:"))
        price=int(input(f"Enter the price of {product_name}:"))
        query="insert into details (Product_name, Quantity, Price) values('%s','%s','%s')"
        args=(product_name, quantity, price)
        data=mydb.execute(query%args)
        con.commit()
        if data:
            print("Item successfully entered")
        else:
            print("something went wrong")

def view_item():
    query="SELECT * FROM details"
    data=mydb.execute(query)
    if data:
        details=mydb.fetchall()
        print(tabulate (details,headers=["Product", "Quantity", "Price"]))
        
    else:
        print("error")

def adminside():
    while True:

        count=1
        menu_list=["Add ITEMS","Remove ITEMS","View ITEMS", "EXIT"]
        for i in menu_list:
            print(f"{count} {i}")
            count+=1
        
        
        user_choice=int(input("Enter your choice:"))

        if user_choice==1:
            add_item_admin()
            
        elif user_choice==2:
            remove_item_admin()
            
        elif user_choice==3:
            view_item()
        else:
            print("exit")
            break

def add_item_user():
    login="rudhra"
    view_item()
    user_input=input("select what you want to buy:")
    query="select * from cart WHERE productname='%s'"
    args=(user_input)
    data=mydb.execute(query%args)
    if data:
        print("product already exists")
        user_quanity=int(input(f"how many {user_input} you want to buy:"))
        query_Q="select Quantity from cart WHERE login_id ='%s' AND productname='%s'"
        args=(login,user_input)
        quantity=mydb.execute(query_Q%args)
        if quantity:
            #quantity update
            cart_quantity=mydb.fetchall()
            print(cart_quantity[0][0])
            new_quantity=cart_quantity[0][0]+user_quanity
            print(f" new quantity:{new_quantity}")
            #price update
            query_p="select price from cart WHERE login_id ='%s' AND productname='%s'"
            args=(login,user_input)
            price=mydb.execute(query_p%args)
            if price:
                new_price=mydb.fetchall()
                print(f"new price{new_price[0][0]}")
                query="UPDATE cart SET price='%s', Quantity='%s' WHERE login_id='%s' AND productname='%s'"
                args_f=(new_price,new_quantity,login,user_input)
                final=mydb.execute(query,args_f)
                if final:
                    print("item successfully added to cart!!!!")
                else:
                    print("there is something wrong!!")
            else:
                print("price error")
        else:
            print("else")        
    else:

        user_quanity=int(input(f"how many {user_input} you want to buy:"))
        query="select * from details where product_name='%s'"
        args=(user_input)
        data=mydb.execute(query%args)
        if data:
            order=mydb.fetchone()
            order_price=order[2]
            order_quantity=order[1]
            print(f"your subtotal {order_price*user_quanity} ruppes!!")
            query= "insert into cart (login_id,productname,Quantity,price) values('%s','%s','%s','%s')"
            total_order=order_price*user_quanity
            args=(login,user_input,user_quanity,total_order)
            data=mydb.execute(query%args)
            
            if data:
                print("product successfully added to cart")
                con.commit()
                new_quantity=order_quantity-user_quanity
                if new_quantity<=0:
                    new_quantity=0
                    query="update details SET Quantity='%s' WHERE Product_name='%s'"
                    args=(new_quantity,user_input)
                    data=mydb.execute(query%args)
                    con.commit()
                    if data:
                        print("success")
                        query="Select * from details WHERE Product_name='%s'"
                        args=(user_input)
                        data=mydb.execute(query%args)
                        if data:
                            mydata=mydb.fetchone()
                            if mydata[1]==0:
                                query="delete from details WHERE product_name='%s'"
                                args=(user_input)
                                data=mydb.execute(query%args)

                                if data:
                                    con.commit()
                    else:
                        print("error")
                else:
                    print("wrong")
            else:
                print("please try again later")
                
        else:
            print("error")


def checkout_user():
    login_id="rudhra"
    query="select * from cart where login_id='%s'"
    args=(login_id)
    data=mydb.execute(query%args)
    if data:
        data=mydb.fetchall()
        print(tabulate(data,headers=["ID","product_name","Quantity","Price"]))
        query="select price from cart WHERE login_id='%s'"
        args=(login_id)
        data=mydb.execute(query%args)
        if data:
            price=mydb.fetchall()
            print(price)
        else:
            print("price error ")
    else:
        print("something went wrong!!")


def remove_item_user():
    login_id="rudhra"
    query="select * from cart where login_id='%s'"
    args=(login_id)
    data=mydb.execute(query%args)
    if data:
        item_remove=input("What you want to remove:")
        item_quantity=int(input(f"how much {item_remove} you want to remove from cart:"))
        query="select * from cart WHERE login_id ='%s' AND productname='%s'"
        args=(login_id,item_remove)
        data=mydb.execute(query%args)
        if data:
            fetch=mydb.fetchall()
            print(fetch)
            if data:
                # fetch_all=mydb.fetchall()
                # print(fetch_all[0][0])
                pass
            else:
                data=mydb.fetchone()
                cart_quantity=data[2]
                if cart_quantity<item_quantity:
                    print(f"you can't remove more than {cart_quantity}")
                else:
                    item_quantity=cart_quantity-item_quantity
                    query="update cart SET Quantity='%s' WHERE login_id='%s' AND productname='%s'"
                    args=(item_quantity,login_id,item_remove)
                    data=mydb.execute(query%args)
                    if data:
                        print("item successfully removed!!")
                        con.commit()
                    else:
                        print("please try again!!")
        else:
            print("something went wrong!!")


add_item_user()

