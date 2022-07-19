import random

a=random.randint(10,20)
count=0
# print(a)

ui=int(input("Enter the number between 10 to 20:"))

keeploop=True

while keeploop == True:

    if a != ui:
        if a<ui:
            print("choose lesser number")
        elif a>ui:
            print("choose higher number")
        
        print("computer wins!")
        count+=1
        ui=int(input("Enter the number between 10 to 20:"))
        

    else:
        print(f"HOLLA you beat the computer with the of {count}")
        print(f"Computer genrated Number is {a}")
        keeploop=False
        break