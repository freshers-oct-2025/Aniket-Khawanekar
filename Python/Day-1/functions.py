def greet():
    print("Hello, Aniket!")
    
greet()

def greet1(name):
    print("Hello,", name)
    
greet1("Aniket")
greet1("NVKDV")

def add(a, b):
    return a + b

res = add(5, 3)
print(res)


def calculate(a, b):
    return a + b, a - b

sum, diff = calculate(10, 5)
print( sum)
print( diff)

def greet2(name="Guest"):
    print("Hello,", name)

greet2("Aniket")
greet2()


def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Aniket")


def outer():
    print("Outer function")

    def inner():
        print("Inner function")
    
    inner()

outer()