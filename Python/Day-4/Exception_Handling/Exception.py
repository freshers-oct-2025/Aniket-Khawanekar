a=5
b=0

try:
    print(a/b)
except ZeroDivisionError as e:
    print("Cannot",e)
except ValueError as e:
    print("Canot",e)
finally:
    print("Thank you")