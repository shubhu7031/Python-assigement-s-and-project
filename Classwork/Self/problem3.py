from getpass import getpass
Creditcard=int((input("Enter the card number: ")))
#password = input("Enter your password:")
password=getpass(prompt="Enter your password:")

print("login successful!! please enter your password to see the full details")


passwd = getpass(prompt="Enter your password")




while True:

    if password==passwd:
        print("login successful")
        break
        
    else:
        passwd = getpass(prompt=" wrong password!  please enter your password:")
 
