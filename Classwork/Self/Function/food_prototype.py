def login(user_name,password):
    if user_name=="ADMIN" and password=="Admin":
        print("-------Welcom admin!------------")
    else:
        print(f"----------welcome {user_name}------------")
        customer_login()

stock={"apple":12,"orange":10,"kiwi":10}
price={"orange":100,"apple":200,"kiwi":100}




def customer_login():

    keeplooping=True
    while keeplooping==True:



        def print_list():
            print("*************************")

            count=0
            for fruit,Quantity in stock.items():
                count+=1
                print(f"{count}   Fruit:{fruit}    Quantity:{Quantity} {price.get(fruit)}.RS")
        
            print("**************************\n\n")

        def user_choice():

            user_choice=int(input("What do you want to buy:"))

            if user_choice==1:
                user_quantity=int(input("how much Quantity you want to buy:"))
                if user_quantity<=stock["apple"]:
                    print(f"{user_quantity} pieces of  apple add to your cart ")
                    print("***************order place successfully*****************")
                    current_stock = stock["apple"] - user_quantity
                    stock["apple"] = current_stock
                else:
                    print(f"not Enough Quantity available")


            if user_choice==2:
                user_quantity=int(input("how much Quantity you want to buy:"))
                if user_quantity<=stock["orange"]:
                    print(f"{user_quantity} pieces of orange add to your cart ")
                    print("***************order place successfully*****************")
                    current_stock = stock["orange"] - user_quantity
                    stock["orange"] = current_stock
                else:
                    print(f"not Enough Quantity available")

            
            if user_choice==3:
                user_quantity=int(input("how much Quantity you want to buy:"))
                if user_quantity<=stock["kiwi"]:
                    print("********************************")
                    print(f"{user_quantity} pieces of kiwi add to your cart ")
                    print("***************order place successfully*****************")
                    current_stock = stock["kiwi"] - user_quantity
                    stock["kiwi"] = current_stock
                else:
                    print(f"not Enough Quantity available")
            
        def choice_menu():
            pass
            #add items
            #remove items
            #view items
            #checkout
            #clear basket
            #exit
            print("1)  Add Item")
            print("2) Remove Item")
            print("3) View Item")
            print("4) Clear basket")
            print("5) Exit")

        
        print_list()
        user_choice()
        choice_menu()

        
    keeplooping==False


    

#main
user_name=input("Enter your user name:").upper()
password=input("Enter your password:")

login(user_name,password)