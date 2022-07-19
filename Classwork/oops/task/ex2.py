class biodata:
    def __init__(self,name,age,gender,college,language):
        self.name = name
        self.age = age
        self.gender = gender
        self.college =college
        self.language = language



access=biodata("shubham","21","male","LDRP",{"php","python","html"})

print(f"{access.name}\n{access.age}\n{access.gender}\n{access.college} \n{access.language}")

