from functools import reduce

num=[1,2,3,4,5,6,7,8,9,10]


squared=list(map(lambda x:x**2,num))
squared1=map(lambda x:x**2,num)
print(squared1)
print("Squared Numbers:", squared)


evens=filter(lambda x:x%2==0,num)
print(evens)
evens_list=list(filter(lambda x:x%2==0,num))
print("Even Numbers:", evens_list)

def apply_operation(func, a,b):
    return func(a,b)

def add(x,y):
    return x+y

def multiply(x,y):
    return x*y  


res_add=apply_operation(add,5,3)
res_multiply=apply_operation(multiply,5,3)
print("Addition Result:", res_add)
print("Multiplication Result:", res_multiply)


n=[5,0,3,8,6]


sum_all = reduce(lambda x, y: x + y, n)
print("Sum using reduce:", sum_all)

doubled = list(map(lambda x: x * 2, n))
print("Doubled numbers:", doubled)

greater_than_4 = list(filter(lambda x: x > 4, n))
print("Numbers greater than 4:", greater_than_4)