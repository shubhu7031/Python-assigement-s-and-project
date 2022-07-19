from tkinter import *
from main_logic import *

user_score_int=IntVar(screen,0)
user_score_int.set(user_score)
computer_score_int=IntVar(screen,0)
computer_score_int.set(computer_score)



lbl_title=Label(text="Rock Paper Scissor",font=("times new roaman",16,"bold"),fg="black")
lbl_title.pack()

rock_btn=Button(text="Rock",font=("times new roaman",16,"bold"),bg="purple",fg="blue",bd=18,activebackground="black",activeforeground="white",height="1",width="7",command=lambda:myfun("rock"))
rock_btn.place(x=20,y=50)

paper_btn=Button(text="paper",font=("times new roaman",16,"bold"),bg="purple",fg="blue",bd=18,activebackground="black",activeforeground="white",height="1",width="7",command=lambda:myfun("paper"))
paper_btn.place(x=180,y=50)

scissor_btn=Button(text="scissor",font=("times new roaman",16,"bold"),bg="purple",fg="blue",bd=18,activebackground="black",activeforeground="white",height="1",width="7",command=lambda:myfun("scissor"))
scissor_btn.place(x=340,y=50)

user_lbl=Label(text="User:",font=("times new roaman",20,"bold"),fg="black",bg="white")
user_lbl.place(x=20,y=150)

user_ans=Label(textvariable=var_userSelection,font=("times new roaman",20,"bold"),fg="black",bg="white")
user_ans.place(x=200,y=150)


#---------------------------------computer-----------------------

computer_lbl=Label(text="Computer:",font=("times new roaman",20,"bold"),fg="black",bg="white")
computer_lbl.place(x=20,y=250)

computer_ans=Label(textvariable=var_computerSelection,font=("times new roaman",20,"bold"),fg="black",bg="white")
computer_ans.place(x=200,y=250)

user_lbl_score=Label(textvariable=user_score_int,font=("times new roaman",20,"bold"),fg="black",bg="white")
user_lbl_score.place(x=400,y=150)


computer_lbl_score=Label(textvariable=computer_score_int,font=("times new roaman",20,"bold"),fg="black",bg="white")
computer_lbl_score.place(x=400,y=250)


final_lbl=Label(textvariable=var_final,font=("times new roaman",30,"bold"),fg="red",bg="white")
final_lbl.place(x=150,y=350)


btn_result= Button(text="Restart",font=("times new roaman",16,"bold"),bg="purple",fg="blue",height=1,width=30,bd=18,activeforeground="black",activebackground="white")
btn_result.place(x=30,y=450)



screen.mainloop()
