import pymysql

con=pymysql.connect(host="localhost",user="root",password="",database="bank")

mydb=con.cursor()

mydb.execute("create table bank (ID integer primary key auto_increment,name varchar(20),gender varchar(20),age varchar(20),current_bal varchar(20),login_id varchar(20),password varchar(20))")


con.commit()