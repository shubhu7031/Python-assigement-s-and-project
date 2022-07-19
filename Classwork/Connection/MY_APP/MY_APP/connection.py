import pymysql

con = pymysql.connect(host="localhost",user="root",password="")

mydb = con.cursor() 

mydb.execute("create database topsapp ")
con.commit()

con = pymysql.connect(host="localhost",user="root",password="",database="topsapp")
mydb = con.cursor()


mydb.execute("create table vaccination_user (id integer primary key auto_increment,firstname varchar(20),lastname varchar(20),age varchar(10),gender varchar(20),doze varchar(20) )")



con.commit()
