def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def factorial(n):
    if n < 0:
        print("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(number):
    return number % 2 == 0



print(greet("Aniket"))
print("Sum:", add(5, 3))
print("Factorial:", factorial(5))
print("Is 4 even?", is_even(4))