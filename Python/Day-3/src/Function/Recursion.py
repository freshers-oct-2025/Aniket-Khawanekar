

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print("Factorial of 5 is:",fact(5))


