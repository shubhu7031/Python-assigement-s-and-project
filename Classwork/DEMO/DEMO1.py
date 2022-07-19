a=[]

for x in range(10000):
    a.append(f"{x}")



a1=1000
b=75

for x in range(a1):
    if x==b:
        index=a.index(b)
        print(f"number found on {index}")
        break
    else:
        print(x)


