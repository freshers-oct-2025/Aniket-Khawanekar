import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds.")
        return result
    return wrap

@timer
def slow_function():
    time.sleep(2)
    print("Function complete.")
slow_function()