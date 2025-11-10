def power(n):
    
    def raise_to(exp):
        return n ** exp
    return raise_to

square = power(4)
result = square(2)
print("4 raised to the power 2 is:", result)
