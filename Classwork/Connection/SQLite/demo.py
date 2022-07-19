import sqlite3

obj=sqlite3.connect('productmanager.db')

cur=obj.cursor()

# user_id="shubhu"
# password="shubhu@7031"
# role="admin"
# cur.execute("create table login (login_id varchar(20),password varchar(20),Role varchar(20))")
# data=cur.execute("insert into login values(? ,?,?)",(user_id,password,role))
# print(data)
# obj.commit()
# data=cur.execute("select Role from login where login_id=:login",{"login":user_id})
# print(data.fetchone())

# cur.execute("update login set Role=:role Where login_id=:login",{"role":"user","login":"shubhu"})
# obj.commit()

# cur.execute("delete from login")
# obj.commit()
obj.close()