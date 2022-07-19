def sum(*value):
    ans=0
    for i in value:
        ans=ans+i
    print(ans)


def sub(num,*value):
    sub=num
    for i in value:
        sub=sub-i
    print(sub)




def mul(num,*value):
    mul=num
    for i in value:
        mul=mul*i
    print(mul)



def div(num,*value):
    div=num
    for i in value:
        if i==0:
            print("can't divisible by zero")
        else:
            div=div/i
            print(div)

   


def cal1():
    keeplooping=True

    while(keeplooping):

        print("Enter 1 for sum")
        print("Enter 2 for sub")
        print("Enter 3 for mul")
        print("Enter 4 for div")

        op=(int(input("Enter the option:")))


        if op ==1:
            
            print("sum")
            sum(10,20,30)
        elif op ==2:
            print("sub")
            sub(10,20,30)
        elif op ==3:
            print("mul")
            mul(10,20,30)
        elif op ==4:
            print("div")
            div(10,20,30)
        else:
            print("nahi med pade")
            keeplooping=False
            break


cal1()
