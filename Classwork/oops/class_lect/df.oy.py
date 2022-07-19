class a:
    def inputa(self):
        self.num1=input("enter")

class b:
    def inputb(self):
        self.num2=input("enter")


class c(a,b):
    def sum(self):
        self.ans=self.num2+self.num1
        print(self.ans)

obj=c()

obj.inputa()
obj.inputb()
obj.sum()
     