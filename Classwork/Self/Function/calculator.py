
def sum(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    if num2<0:
        print("number is not divide by zero")
    else:
        return num1/num2



def cal():

    num1=(int(input("Enter the first number:")))
    num2=(int(input("Enter the second number:")))

    
    keeplooping=True

    while keeplooping:
        
        print("Enter 1 for sum")
        print("Enter 2 for sub")
        print("Enter 3 for mul")
        print("Enter 4 for div")

        op=(int(input("Enter the option:")))



        if op==1:
            ans=sum(num1,num2)
            print(ans)
        
        elif op==2:
            ans=sub(num1,num2)
            print(ans)
        
        elif op==3:
            ans=mul(num1,num2)
            print(ans)
        
        elif op==4:
            
            ans=div(num1,num2)
            print(ans)
            
    else:
        keeplooping=False
       # break

cal()
