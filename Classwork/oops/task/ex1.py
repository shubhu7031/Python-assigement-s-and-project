class cal:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I got called")

    def __str__(self):
        return "I am a class"

sum=cal(5,2)
print(sum.a+sum.b)

sub=cal(5,2)
print(sub.a-sub.b)

mul=cal(5,2)
print(mul.a*mul.b)

print(mul)

div=cal(5,2)
print(div.a/div.b)

