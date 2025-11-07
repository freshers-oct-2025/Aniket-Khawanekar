
def Fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f


print("Factorial is:",Fact(5))