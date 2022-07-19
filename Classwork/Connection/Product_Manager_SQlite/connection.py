import sqlite3

con=sqlite3.connect('productmanager.db')

mydb=con.cursor()

#mydb.execute("create table login (login_id varchar(20),password varchar(20),Role varchar(20))")
#mydb.execute("create table details (productname varchar(20),Quantity varchar(20),price varchar(20))")
#mydb.execute("create table Cart (login_id varchar(20),productname varchar(20),Quantity Integer,price Integer)")

con.commit()
con.close()