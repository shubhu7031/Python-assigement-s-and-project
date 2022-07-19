import pymysql
from tkinter import *
from datetime import date


con = pymysql.connect(host="localhost",user="root",password="",database="topsapp")
db = con.cursor()


root = Tk()
root.geometry("500x500")
root.title("Data Entry")

fname = StringVar()
lname = StringVar()
gender = StringVar()
age = StringVar()
v_c = StringVar()
search_update_var = StringVar()

date = date.today()
date = str(date)

result_var = StringVar()

#--------------------- to store data in database 

def insertData():
    firstname = fname.get()
    lastname = lname.get()
    age_v = age.get()
    gender_v = gender.get()
    doze = v_c.get()

    query="insert into vaccination_user (firstname,lastname,age,gender,doze) values ('%s','%s','%s','%s','%s')"
    args = (firstname,lastname,age_v,gender_v,doze)

    data = db.execute(query%args)
    if data:
        result_var.set("Successfully data inserted !!!")
    else:
        result_var.set("Something went wrong  !!!")
    con.commit()


def searchData():
    name = search_update_var.get()
    query = "select * from vaccination_user where (firstname='%s')"
    args = (name)


    db.execute(query%args)
    result= db.fetchone()
    print(result[1])
    print(result[2])
    print(result[3])
    print(result[4])
    print(result[5])

    


# -----------------------------------------------------end store db 


# Label First Name
label_fname = Label(root, text="First Name : ")
label_fname.place(x=50, y=80)
# Entry First Name
entry_fname = Entry(root, textvariable=fname)
entry_fname.place(x=180, y=80)

# Label Last Name
label_lname = Label(root, text="Last Name : ")
label_lname.place(x=50, y=110)
# Entry Last Name
entry_lname = Entry(root, textvariable=lname)
entry_lname.place(x=180, y=110)

# Label gender
label_gender = Label(root, text="Gender : ")
label_gender.place(x=50, y=140)
# Entry gender
entry_gender = Entry(root, textvariable=gender)
entry_gender.place(x=180, y=140)

# Label age
label_age = Label(root, text="Age : ")
label_age.place(x=50, y=170)
# Entry age
entry_age = Entry(root, textvariable=age)
entry_age.place(x=180, y=170)

# Label vaccination_dose
label_vaccination_dose = Label(root, text="Vaccination_dose  : ")
label_vaccination_dose .place(x=50, y=200)

# Entry vaccination_dose
entry_vaccination_dose = Entry(root, textvariable=v_c)
entry_vaccination_dose .place(x=180, y=200)

# Submit Button
insert = Button(root, text="SUBMIT", bg="black", fg="white", command=insertData)
insert.place(x=50, y=250)


result = Label(root,textvariable=result_var,fg="black")
result.place(x=50,y=280)

# Label vaccination_dose
search_lbl = Label(root, text="Search : ")
search_lbl.place(x=50, y=280)

# Entry vaccination_dose
search_entry = Entry(root,textvariable=search_update_var)
search_entry.place(x=250, y=280)


search = Button(root, text="Search", bg="black", fg="white", command=searchData)
search.place(x=300, y=250)

update = Button(root, text="Update", bg="black", fg="white", command=insertData)
update.place(x=350, y=250)


root.mainloop()