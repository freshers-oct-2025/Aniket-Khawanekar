def number_generator(n):
    for i in range(n):
        yield i

def even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 2

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Number generator:")
for num in number_generator(5):
    print(num)

print("\nEven numbers:")
for even in even_numbers(10):
    print(even)

print("\nFibonacci sequence:")
for fib in fibonacci(6):
    print(fib)