from random import randint
import bank 
import smtplib


def SendEmail(to,content):
    # for sending a Email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rroot310@gmail.com', 'RRooT@#$310')
    server.sendmail('rroot310@gmail.com',to, content)
    server.close()
# mainf is the main function that runs after validate Email Address

def mainf(): 
    otp=randint(0000,9000)
    print(otp)  
    count=0
    
    to=input("Enter the email address to continue:")
    content=f"Your otp for the apni bank is {otp}"
    SendEmail(to,content)


    user_otp=int(input("Enter the otp"))
    while count<4:
        
        if user_otp==otp:
            print("login successfully!!")
            content="you have successfully logged in to the apni bank"
            SendEmail(to,content)

            bank.bank()
            break
        else:
            print("login unsuccessful")
            count+=1
            otp=randint(0000,9000)
            content=f"your OTP for the apni bank is {otp}"


            print(content)
            SendEmail(to,content)


            print(f"you have {count-3} tries left to login")

            user_otp=int(input("Enter the OTP again:"))
            if count==3:
                print("your action has been blocked")
                break
            

print("welcome  to the apni Bank\nplease enter the otp to process further")
mainf()