class human:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def printdata(self):
        print(f"your first name is:{self.fname}\nyour last name is:{self.lname}")


class display(human):
   pass

obj=display("shubham","mevada")

obj.printdata()