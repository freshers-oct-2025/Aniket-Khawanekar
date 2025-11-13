class Computer:
    def __init__(self,cpu,ram):
        self.cpu= cpu
        self.ram= ram   

    def config(self):
        print("Configuration is:",self.cpu,self.ram)

comp1=Computer('i5',16)
comp2=Computer('Ryzen 5',8)


# comp1=Computer()
# comp2=Computer()
print(type(comp1))

# Computer.config(comp1)
# Computer.config(comp2)

comp1.config()
comp2.config()