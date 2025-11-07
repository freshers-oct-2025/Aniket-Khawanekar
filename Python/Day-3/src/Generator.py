def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)
    
    
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

   
    fib = fibonacci()
    for _ in range(5):
        print(next(fib))