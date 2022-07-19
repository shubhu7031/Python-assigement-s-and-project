from tkinter import *
import datetime
from tkinter import messagebox

screen=Tk()
screen.geometry("500x500")

fname=StringVar()
lname=StringVar()
age=StringVar()
gender=StringVar()
vaccination=StringVar()

#fname
lbl_fname=Label(screen,text="Enter your name:")
lbl_fname.place(x=50,y=80)

e1=Entry(screen,width=20,textvariable=fname)
e1.place(x=200,y=80)

#lanme
lanme_lbl=Label(screen,text="Enter your last name:")
lanme_lbl.place(x=50,y=110)

e2=Entry(screen,width=20,textvariable=lname)
e2.place(x=200,y=110)

#age
age_lbl=Label(screen,text="Enter your age:")
age_lbl.place(x=50,y=140)

e2=Entry(screen,width=20,textvariable=age)
e2.place(x=200,y=140)

#gender
gender_lbl=Label(screen,text="Enter your Gender:")
gender_lbl.place(x=50,y=170)

e2=Entry(screen,width=20,textvariable=gender)
e2.place(x=200,y=170)

#vaccination
age_lbl=Label(screen,text=" vaccination doze:")
age_lbl.place(x=50,y=200)

e2=Entry(screen,width=20,textvariable=vaccination)
e2.place(x=200,y=200)






def myfun():
    date=datetime.date.today()
    date=str(date)
    file=open(date,"a")

    if fname.get()=="" or lname.get()=="" or age.get()=="" or gender.get()=="" or vaccination.get()=="":
        messagebox.showerror("Error","All fields are mandatory")
    else:
        print(f"fname:{fname.get()}")
        print(f"lname:{lname.get()}")
        print(f"age:{age.get()}")
        print(f"gender:{gender.get()}")
        print(f"vaccincation:{vaccination.get()}")

        data=f"firstname : {fname.get()}\nlastname : {lname.get()}\nage : {age.get()}\ngender : {gender.get()}\nvaccination : {vaccination.get()}\n\n"
        file.write(data)
        file.close()


btn=Button(screen,text="submit",command=myfun)
btn.place(x=50,y=250)

screen.mainloop()

