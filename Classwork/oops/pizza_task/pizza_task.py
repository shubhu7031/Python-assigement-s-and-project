class pizzeria:

    free_cock=0
    total_order=0
    payment_pizza=0
    payment_pasta=0
    free_bruschetta=0
    chocco_brownies=0
    number_pizza=0
    number_pasta=0
    

    def menu(self):
        main_menu="""

    1 large pizza = 10.99 AUD 

    2 large Pizzas = 20.99 AUD 

    3 Large Pizzas = 29.99 AUD

    ***Buy 4 or more pizza and get 1.5lt of soft drink free***


    1 large pasta = 9.5 AUD 

    2 large pastas = 17.00 AUD 

    3 large pastas = 27.50 AUD

    ***Buy 4 or more pastas and get 2 bruschetta free.***

    ***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free."""
        print(main_menu)
    def user_side(self):
        
        Cust_name=input("enter your name:")



        #PIZZA
        print(f"Welcome {Cust_name} to the pizza shop:")
        pizza_order=int(input("please select the pizza you want:"))



        if pizza_order==1:
            print(f"your total for the {pizza_order} pizza is 10.99 AUD")
            self.total_order=self.total_order+10.99
            self.payment_pizza=self.payment_pizza+10.99
            self.number_pizza=self.number_pizza+1


        elif pizza_order==2:
            print(f"your total for the {pizza_order} pizza is 20.99 AUD")
            self.total_order=self.total_order+20.99
            self.payment_pizza=self.payment_pizza+20.99
            self.number_pizza=self.number_pizza+2



        elif pizza_order==3:
            print(f"your total for the {pizza_order} pizza is 29.99 AUD")
            self.total_order=self.total_order+29.99
            self.payment_pizza=self.payment_pizza+29.99
            self.number_pizza=self.number_pizza+3

    
        else:
            print("*** Congratulations !! 1.5lt softdrink free *** ")
            self.free_cock=self.free_cock+1
            print(f"your total for the {pizza_order} pizza is {pizza_order*10.99} AUD")
            self.total_order=self.total_order+pizza_order*10.99
            self.payment_pizza=self.payment_pizza+pizza_order*10.99
            self.number_pizza=self.number_pizza+pizza_order





            
        #PASTA
        pasta_order=int(input("please select the pasta you want"))
        if pasta_order==1:
            print(f"your total for the {pasta_order} pasta is 9.5 AUD")
            self.total_order=self.total_order+9.5
            self.payment_pasta=self.payment_pasta+9.5
            self.number_pasta=self.number_pasta+1


        elif pasta_order==2:
            print(f"your total for the {pasta_order} pasta is 17.00 AUD")
            self.total_order=self.total_order+17.00
            self.payment_pasta=self.payment_pasta+17.00
            self.number_pasta=self.number_pasta+2


        elif pasta_order==3:
            print(f"your total for the {pasta_order} pasta is 27.50 AUD")
            self.total_order=self.total_order+27.50
            self.payment_pasta=self.payment_pasta+27.50
            self.number_pasta=self.number_pasta+3


        elif pasta_order>=4:
            print("*** Congratulations !! get 2 bruschetta free *** ")
            self.total_order=self.total_order+pasta_order*9.5
            print(f"your total order is {pasta_order*9.5}")
            self.payment_pasta=self.payment_pasta+pasta_order*9.5
            self.free_bruschetta=self.free_bruschetta+2
            self.number_pasta=self.number_pasta+pasta_order


        elif pasta_order and pizza_order>=4:
            print("*** Congratulations !! get 2 chocco brownies ice cream free ***")
            self.total_order=self.total_order+pasta_order*9.5
            self.payment_pasta=self.payment_pasta+pasta_order*9.5
            self.chocco_brownies=self.chocco_brownies+2
            self.number_pasta=self.number_pasta+pasta_order

        print(f"your total order is {self.total_order}")
        print(f"-----> your Net order amount of the day is : {self.total_order}")

    


        customer_input=input("do you want to enter a order from another customer:")

        if customer_input.startswith("y") or customer_input.startswith("Y"):
            obj.user_side()
        else:
            print("----------- Pizza and pasta Bill --------------")

            print(f"Number of 1.5lt soft drink bottles given:{self.free_cock}")
            print(f"total payment received today:{self.total_order}")
            print(f"payment received from pasta:{self.payment_pasta}")
            print(f"payment received from pizza:{self.payment_pizza}")
            print(f"Number of bruschetta given to customer:{self.free_bruschetta}")
            print(f"Number of chocco brownies ice cream given to customer:{self.chocco_brownies}")
            print(f"Number of pizza and pasta sold in one shift {self.number_pizza+self.number_pasta}")
            print("bye bye")
obj=pizzeria()

print("prees 1 : for menu")
print("press 2 : exit")
user_input=int(input("Enter your choice:"))
if user_input==1:
    obj.menu()
    obj.user_side()
else:
    print("bye bye")