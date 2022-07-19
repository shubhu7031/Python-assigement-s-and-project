# Login Menu
### --- are you a customre
### --- are you a product manager
# -------------------------------------------
managerID = "admin"
managerPassword = "admin"

availableStock = {"Apple" : 50, "Banana" : 35, "Kiwi" : 10, "Orange" : 50}     # "stock" : quantity
stockPrice = {"Apple" : 10, "Banana" : 5, "Kiwi" : 20, "Orange" : 5}         # "stock" : price
managerMenuOptions = {
    1 : "Add ITEMS",
    2 : "Remove ITEMS",
    3 : "View ITEMS",
    4 : "EXIT"
}


customerStock = {}      # "stock" : quantity
customerPrice = {}      # "stock" : price
customerMenuOptions = {
    1 : "Add ITEMS",
    2 : "Remove ITEMS",
    3 : "View ITEMS",
    4 : "CHECKOUT",
    5 : "Clear BASKET",
    6 : "EXIT"
}




def mainLogin ():

    reStart = True
    
    while reStart:

        print("\n\n\n\tH I N T : If you are a Manager, Yur USERNAME and PASSWORD is 'admin'")
        print("\tH I N T : If you want to QUIT the Programme, the USERNAME and PASSWORD is 'quit'\n\n")
            
        userId = input("USERNAME :\t").lower()
        userPassword = input("PASSWORD :\t").lower()
    
        if userId == managerID and userPassword == managerPassword:
            managerLogin()
        elif userId.startswith("q") and userPassword.startswith("q"):
            reStart = False
            print("\n\n\n\n\t\t**** THANK YOU FOR USING OUR SERVICES ****\n\n\n")
        else:
            customerLogin()

# IF CUSTOMER
## --- Choose from the following basket of fruits                   
## --- What do you want to buy DISPLAY ITEMS + PRICE                            DONE
## --- How much quantity do you want to buy                                     DONE
## --- CHECK IF ENOUGH QUANTITY AVAILABLE                                       DONE

## --- IF ORDER QUANTITY == AVAILABLE QUAANTITY                                 DONE
### --- Execute order                                                           DONE
### --- Remove that quantity from available stock                               DONE
### --- Ask if want to add more items in the basket                             
### --- Show Bill

## --- IF ORDER QUANTITY != AVAILABLE QUAANTITY
### --- ERROR LOW QUANTITY
### --- SHOW AVAILABLE STOCK
### --- Ask if want to add available items in the basket
### --- Execute order
### --- Ask if want to add more items in the basket
### --- Show Bill
# -------------------------------------------

def display_availableStockItems ():
    counter = 1
    
    for fruits, quantity in availableStock.items():
        print(f"{counter})\t{fruits}\t{quantity} pcs")
        counter += 1

def display_availableStockPrice ():
    counter = 1
    
    for fruits, quantity in availableStock.items():
        print(f"{counter})  {fruits}\t{quantity} pcs\tRs.{stockPrice.get(fruits)} each")
        counter += 1





def display_customerStockItems ():
    counter = 1
    
    for fruits, quantity in customerStock.items():
        print(f"{counter})\t{fruits.capitalize()}\t{quantity} pcs")
        counter += 1       
    
def display_customerStockPrice ():
    counter = 1
    amountToPay = 0
    
    for fruits, prices in customerPrice.items():
        print(f"{counter})\t{fruits.capitalize()}\t {customerStock.get(fruits)} Pcs for Rs.{stockPrice.get(fruits)} each")
        counter += 1
        amountToPay += prices

    print(f"Total amount Payable is Rs.{amountToPay}")

def customer_addItems ():
    # Will add quantity only 
    # No option to view cart or remove items
    print("What do you want to buy today?\n\n")
    
    # Display Available stock and its price (USING "stockPrice" Dict)
    display_availableStockPrice()
    
    # Get item number
    customer_addItemNumber = int(input("\nPlease select the item you want to add:\t")) - 1
    
    # Get item name
    keys_list = list(stockPrice)
    customer_addItemName = keys_list[customer_addItemNumber]

    # Get item quantity to add
    while True:
        
        # Get item quantity to add
        customer_addItemQuantity = int(input(f"\nPlease enter how many {customer_addItemName}s you want to add:\t"))

        if customer_addItemQuantity > 0:                                                        # IF = QUANTITY > 0
            if availableStock.get(customer_addItemName) > 0:                                    # IF = ITEM IN STOCK
                if customer_addItemQuantity <= availableStock.get(customer_addItemName):        # IF = ENOUGH QUANTITY AVAILABLE IN STOCK

                    # EXECUTE ORDER
                    print("\n\n\t\t*****\tOrder Successful\t*****\n\n")

                    # Remove items from stock
                    availableStock[customer_addItemName] = availableStock.get(customer_addItemName) - customer_addItemQuantity
                    
                    # Remove empty items from the list
                    if availableStock.get(customer_addItemName) == 0:
                        availableStock.pop(customer_addItemName)
                        
                    if customer_addItemName not in customerStock:                               # IF = ITEM ALREADY EXIST IN CUSTOMER BASKET
                        customerStock[customer_addItemName] = customer_addItemQuantity          # IF NOT = ADD NEW 
                        customerPrice[customer_addItemName] = (customer_addItemQuantity * stockPrice.get(customer_addItemName))
                    else:                                                                       # ELSE   = UPDATE BASKET
                        customerStock[customer_addItemName] = customerStock.get(customer_addItemName) + customer_addItemQuantity
                        customerPrice.update({customer_addItemName : (customer_addItemQuantity * stockPrice.get(customer_addItemName))})
                    break
                    
                

                else:                                                                           # ELSE = ENTER LESSER QUANTITY
                    print("\n\n\t\tERROR\n\n")
                    print("Insufficient Stock")
                    print(f"Current Stock is {availableStock.get(customer_addItemName)}")
                    customer_addItemQuantity = int(input(f"\nQuantity for {customer_addItemName} must be less than {availableStock.get(customer_addItemName)}. ADD AGAIN:\t"))
            else:
                print(f"\n\n\t\t{customer_addItemName.capitalize()}s are out of stock.")        # ELSE = ITEM OUT OF STOCCK
                print("\t\t  SORRY FOR THE TROUBLE")
                break
        else:                                                                                   # ELSE = ENTER QUANTITY > 0
            customer_addItemQuantity = int(input(f"\nQuantity for {customer_addItemName} must be more than 0. ADD AGAIN:\t"))

def customer_removeItems ():
    
    # Will add quantity only 
    # No option to view cart or remove items
    print("What do you want to Remove?\n\n")
    
    
    # Display Available stock and its price (USING "stockPrice" Dict)
    display_customerStockItems()
    
    # Get item number
    customer_removeItemNumber = int(input("Please select the item you want to remove:\t")) - 1
    
    # Get item name
    keys_list = list(customerStock)
    customer_removeItemName = keys_list[customer_removeItemNumber]

    # Get item quantity to add
    while True:
        
        # Get item quantity to add
        customer_removeItemQuantity = int(input(f"\nPlease enter how many {customer_removeItemName}s you want to remove:\t"))

        if customer_removeItemQuantity > 0:                                                        # IF = QUANTITY > 0
            if customerStock.get(customer_removeItemName) > 0:                                     # IF = ITEM IN STOCK
                if customer_removeItemQuantity <= customerStock.get(customer_removeItemName):      # IF = ENOUGH QUANTITY AVAILABLE IN STOCK

                    # EXECUTE ORDER
                    print("\n\n\t\t*****\rRemoved Item Successfully\t*****\n\n")

                    # Add items back to stock
                    availableStock[customer_removeItemName] = availableStock.get(customer_removeItemName) + customer_removeItemQuantity
                    
                    # Remove items from the basket
                    customerStock[customer_removeItemName] = customerStock.get(customer_removeItemName) - customer_removeItemQuantity
                    
                    # Change Price from custoemr price dict
                    for fruits, totalPrice in customerPrice.items(): 
                        customerPrice[fruits] = customerStock.get(fruits) * stockPrice.get(fruits)
                    
                    # Remove empty items from the list
                    if customerStock.get(customer_removeItemName) == 0:
                        customerStock.pop(customer_removeItemName)
                            
                    break
                    
                else:                                                                                           # ELSE = ENTER LESSER QUANTITY
                    print("\n\n\t\tERROR\n\n")
                    print("You cannot remove more than what yo have in your basket")
                    print(f"You currently have {customerStock.get(customer_removeItemName)} in stock")
                    customer_removeItemQuantity = int(input(f"\nQuantity for {customer_removeItemName} must be less than {customerStock.get(customer_removeItemName)}. TRY AGAIN:\t"))
            else:
                print(f"\n\n\t\tYou do not have {customer_removeItemName.capitalize()}s in your basket")        # ELSE = ITEM NOT IN BASKET
                break
        else:                                                                                                   # ELSE = ENTER QUANTITY > 0
            customer_removeItemQuantity = int(input(f"\nQuantity for {customer_removeItemName} must be more than 0. TRY AGAIN:\t"))

def customerLogin ():
    
    keepLooping = True
    
    print("\n\n\t\t*************************")
    print("\t\tWELCOME TO THE FRUIT MART")
    print("\t\t*************************\n\n")
    
    
    while keepLooping:
    
        if len(customerStock) == 0:                                                                     # If the customer's basket is empty 

            customer_addItems()
                        
        else:                                                                                           # ELSE = Customer Basket has items 
        
            print("\n\n")

            
            # Display MENU OPTIONS
            for index, options in customerMenuOptions.items():
                print(f"{index})\t{options}")
            
            customer_menuOption = int(input("Please choose one of the above options:\t"))

            if customer_menuOption == 1:
                
                customer_addItems()
                
                
            elif customer_menuOption == 2:
                
                customer_removeItems()
                
            elif customer_menuOption == 3:
                # View Items
                
                print("\n\n")

                display_customerStockPrice()
                    
                print("\n\n")
            
            elif customer_menuOption == 4:
                # Check Out
                
                checkOut = input("Are you sure you want to checkout?\t").upper()
                
                if checkOut.startswith("Y"):
                    print("\n\nThank you for shopping with us today.\n\n")
                    display_customerStockPrice()
                    print("\n\nHave a great day and hope to see you soon :)\n\n")
                    print("\t\t*************************")
                    print("\t\t     Keep Shopping ;)")
                    print("\t\t*************************")
                    customerStock.clear()
                    customerPrice.clear()

                    keepLooping = False
                
            elif customer_menuOption == 5:
                # CLEAR customer basket and break the loop
                clearBasket = input("Are you sure you want to clear the basket?\t").upper()
                
                if clearBasket.startswith("Y"):
                    customerStock.clear()
                    customerPrice.clear()
                    print("\n\nBASKET EMPTY!!\n\n")
                    print("\t\t*************************")
                    print("\t\t     Keep Shopping ;)")
                    print("\t\t*************************")
            
            elif customer_menuOption == 6:
                # Exit the Loop
                print("\n\nAre you sure you want to Quit without checkout?")
                print("\n\n\t\t!!!All the items in your cart will be lost...!!!\n\n")
                exitLoop = input("'Yes' to EXIT \t\t 'NO' to Continue Shopping:\t").upper()
                
                if exitLoop.startswith("Y"):
                    customerStock.clear()
                    customerPrice.clear()
                    print("\t\t*************************")
                    print("\t\t     Keep Shopping ;)")
                    print("\t\t*************************")
                    keepLooping = False

            else:
                print("Enter Correct Option")


# IF PRODUCT MANAGER
## --- SHOW MENU TO ADD, REMOVE, VIEW STOCK

## IF ADD STOCK
### --- How much quantity do you want to add
### --- ADD and Update new PRICE for all
### --- CONFIRM STOCK ADDED
### --- SHOW ALL STOCK

## IF REMOVE STOCK
### --- How much quantity do you want to remove
### --- CONFIRM STOCK REMOVED
### --- SHOW ALL STOCK

def manager_addItems ():
    
    print("\n\n")
    print("Current Stock is:")
    print("\n\n")
    display_availableStockItems()
    print("\n\n")
    
    manager_addItemName = input("Please enter the name of the item:\t").capitalize()
    manager_addItemQuantity = int(input(f"Please enter the how many {manager_addItemName}s you want to add:\t"))
    manager_addItemPrice = int(input(f"Please enter the price of each {manager_addItemName}:\t"))

    if manager_addItemName in availableStock:
        availableStock[manager_addItemName] = (availableStock.get(manager_addItemName) + manager_addItemQuantity)
    else:
        availableStock[manager_addItemName] = manager_addItemQuantity
    
    stockPrice[manager_addItemName] = manager_addItemPrice

    print("\n\n\t\t**** ITEM ADDED SUCCESSFULLY ****")

    print("\n\n")
    print("NEW Stock is:")
    print("\n\n")
    display_availableStockItems()
    print("\n\n")

def manager_removeItems ():
    
    print("\n\n")
    print("Current Stock is:")
    print("\n\n")
    display_availableStockItems()
    print("\n\n")

    # Get item number
    manager_removeItemNumber = int(input("Please select the item you want to remove:\t")) - 1
    
    # Get item name
    keys_list = list(availableStock)
    manager_removeItemName = keys_list[manager_removeItemNumber]

    
    while True:
        manager_removeItemQuantity = int(input(f"Please enter the how many {manager_removeItemName}s you want to remove:\t"))
    
        if availableStock.get(manager_removeItemName) >= manager_removeItemQuantity:
            availableStock[manager_removeItemName] = (availableStock.get(manager_removeItemName) - manager_removeItemQuantity)
            break
        else:
            print("\n\n! ! ! E R R O R ! ! !")    
            print("\nYou cannot remove more than whhat is in the stock")    
            print(f"\n\nAvailable stock of {manager_removeItemName} is currently {availableStock.get(manager_removeItemName)}")    
            print(f"\nPlease try again by entering a lesser quantity than {availableStock.get(manager_removeItemName)}...")
    
    if availableStock.get(manager_removeItemName) <= 0:
        availableStock.pop(manager_removeItemName)
    else:
        priceUpdateOnReomove = input(f"Do you want to update thee price of {manager_removeItemName}?\t").upper()

        if priceUpdateOnReomove.startswith("Y"):
            manager_removeItemPrice = int(input(f"Please enter the NEW price for {manager_removeItemName}s:\t"))
            stockPrice[manager_removeItemName] = manager_removeItemPrice
            print("\n\n\t\t**** PRICE UPDATED SUCCESSFULLY ****\n\n")

    
    print("\n\n\t\t**** ITEM REMOVED SUCCESSFULLY ****")

    print("\n\n")
    print("NEW Stock is:")
    print("\n\n")
    display_availableStockItems()
    print("\n\n")

def managerLogin ():
    
    keepLooping = True
    
    print("\n\n\t\t*************************")
    print("\t\tWELCOME TO THE FRUIT MART")
    print("\t\t*************************\n\n")
    
    print("Your current stock is:\n\n")
    display_availableStockPrice()
    print("\n\n")
    
    while keepLooping:
    
        # Display MENU OPTIONS
        for index, options in managerMenuOptions.items():
            print(f"{index})\t{options}")
        
        manager_menuOption = int(input("Please choose one of the above options:\t"))

        if manager_menuOption == 1:
            # Add Items
            manager_addItems()
            
            
        elif manager_menuOption == 2:
            # Remove Items
            manager_removeItems()
            
        elif manager_menuOption == 3:
            # View Items
            
            print("\n\n")

            display_availableStockPrice()
                
            print("\n\n")
        
        elif manager_menuOption == 4:
            # Exit the Loop
            exitLoop = input("\n\nAre you sure you want to Quit?\t").upper()
            
            if exitLoop.startswith("Y"):
                print("\n\n")
                print("\t\t*************************")
                print("\t\t       THANK YOU")
                print("\t\t*************************")
                print("\n\n")
                keepLooping = False

        else:
            print("Enter Correct Option")




mainLogin()