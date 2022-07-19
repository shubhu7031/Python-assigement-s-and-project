from tkinter import *

screen=Tk()
screen.geometry("500x500")

btn=Button(screen,text="1",height=2,width=2)
btn.grid(row=0,column=0,padx=10,pady=10)

btn=Button(screen,text="2",height=2,width=2)
btn.grid(row=0,column=1)

btn=Button(screen,text="3",height=2,width=2)
btn.grid(row=1,column=0)

btn=Button(screen,text="4",height=2,width=2)
btn.grid(row=1,column=1)

btn=Button(screen,text="5",height=2,width=2)
btn.grid(row=1,column=2)

screen.mainloop()
