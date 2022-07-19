import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="topsapp")

mydb=con.cursor()

mydb.execute("create table Metadata (ID integer primary key auto_increment,Fname varchar(20),lname varchar(20),gender varchar(20),age varchar(20))")



con.commit()