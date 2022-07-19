import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="productmanager")

mydb=con.cursor()


#mydb.execute("create database productmanager")

#mydb.execute("create table login (Login_id varchar(20),password varchar(20),role varchar(20))")

#mydb.execute("create table details (Product_name varchar(20),Quantity Integer,Price Integer)")

mydb.execute("create table Cart (login_id varchar(20),productname varchar(20),Quantity Integer,price Integer)")

con.commit()
