from tkinter import *
import random


screen=Tk()
screen.geometry("500x600")
screen.title("Rock Paper Scissor")




'''

computer_score=IntVar()
computer_score.set(0)

user_score=IntVar()
user_score.set(0)
'''
user_score=0
computer_score=0


result=""




var_userSelection=StringVar()
var_userSelection.set("PENDING!!!")

var_computerSelection=StringVar()
var_computerSelection.set("PENDING!!!")

var_final=StringVar()
var_final.set("PENDING!!!")

list=["rock","paper","scissor"]



def myfun(user):
    global user_score,computer_score
    var_userSelection.set(user)
    computer_choice=random.choice(list)
    var_computerSelection.set(computer_choice)
    
    

    if user == "rock":
        if computer_choice =="paper":
            #var_final.set("Computer wins!!!!!")
            computer_score=computer_score+1
           
            
        elif computer_choice=="scissor":
            #var_final.set("User wins!!!")
            user_score=user_score+1
          
            
        elif computer_choice=="rock":
            #var_final.set("Match Tie!!!")
            pass


    elif user =="paper":
        if computer_choice=="rock":
            #var_final.set("User wins!!!")
            user_score=user_score+1
       
            
        elif computer_choice=="scissor":
            #var_final.set("Computer wins!!!")
            computer_score=computer_score+1
      
            
        elif computer_choice=="paper":
            #var_final.set("match tie!!!")
            pass
    
    elif user =="scissor":
        if computer_choice=="rock":
            #var_final.set("Computer wins!!!")
            computer_score=computer_score+1
            
        elif computer_choice=="paper":
            #var_final.set("User wins!!!")
            user_score=user_score+1
            
        elif computer_choice=="scissor":
            #var_final.set("match tie!!!")
            pass

    if user_score==10:
        var_final.set("User wins!!!")
    elif computer_choice==10:
        var_final.set("Computer wins!!!")
    print(user_score)
    print(computer_score)




    