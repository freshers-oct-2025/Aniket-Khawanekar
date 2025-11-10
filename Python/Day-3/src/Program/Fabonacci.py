
def fab(n):
    a,b=0,1
    if n<=0:
        print("Invalid input")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fab(5)