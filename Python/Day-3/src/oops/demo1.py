class Computer:
    
    ram=8
    def __init__(self):
        self.name="Aniket"
        self.age=24
        


c1=Computer()
c2=Computer()

c1.name="Khawanekar"
c1.age=25

print(c1.name)  
print(c1.age)
print(id(c1))
print(id(c2))