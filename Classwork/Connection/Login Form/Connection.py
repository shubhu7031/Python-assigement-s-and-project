import pymysql

con = pymysql.connect(host="localhost",user="root",password="",database="topsapp")

mydb = con.cursor()


mydb.execute("create table details (id integer primary key auto_increment,login_id varchar(20),password varchar(20))")



con.commit()
