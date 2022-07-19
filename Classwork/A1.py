age=int(input("Enter your Age:"))
while True:
    print(True if age>=18 else False)
    if age>=18:
        break
    else:
        age=int(input("Enter your Age:"))
