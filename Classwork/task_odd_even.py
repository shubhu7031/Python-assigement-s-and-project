keeplooping="True"
while keeplooping:
    print("1) for odd number")
    print("2) for even number")
    print("3) for prime number")
    print("4) for exit")

    def alone(num):
        if (num%2==0):
            print(f"{num} is odd number")
        else:
            print(f"{num} is even number")
    
    def prime(num):
        if num > 1:
            for i in range(2, num//2):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
                else:
                    print(num, "is a prime number")
        else:
            print(num, "is not a prime number")





    choice=int(input("Enter your choice:"))
    
    if choice ==1:
        value=int(input("Enter number:"))
        alone(value)
        oddlist=[x for x in range(value) if x % 2==0]
        print(f"list of odd number in  range of {value}\n {tuple(oddlist)}") 



    elif choice ==2:
        value=int(input("Enter number:"))
        alone(value)
        evenlist=[x for x in range(value) if x % 2!=0]
        print(f"list of even number in  range of {value}\n {tuple(evenlist)}")
    
    elif choice==3:
        value=int(input("Enter the number:"))
        prime(value)
        l = range(1,value)
        primelist=[item for item in l if item>1 and len([i for i in range(2,item) if item%i==0])==0]        
        print(f"list of prime number in  range of {value}\n {tuple(primelist)}")     
    else:
        keeplooping="false"
        break
