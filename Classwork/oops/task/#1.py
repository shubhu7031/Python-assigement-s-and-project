#class and object 

class Dog:
    def __init__(self,name,age,gender):
        self.name = name
        self.age=age
        self.gender = gender


obj=Dog("lebra",15,"fe  male")

print(f"{obj.name}\n{obj.age}\n{obj.gender}")
obj.name="Shubham"
obj.age=20
obj.gender="male"
print(f"{obj.name}\n{obj.age}\n{obj.gender}")


