from tkinter import *

screen=Tk()
screen.geometry("500x500")
screen.title("OTP system")

email_id=StringVar()


main_lbl=Label(screen,text="Enter your email id:")
main_lbl.place(x=50,y=80)

e1=Entry(screen,width=20,textvariable=email_id)
e1.place(x=200,y=80)

btn=Button(screen,text="submit")
btn.place(x=272,y=36)

                            
screen.mainloop()
