# Problem: Write a decorator that measures the time a function takes to execute.

# decorator are like higher order function like in Js

import time

# accepting func as parameter
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # func.__name__ to know the name of the function caller or function name
        print(f"{func.__name__} ran in {end - start}time")
        return result
    return wrapper


# decorating this example_func so it will only pass being the timer()
# takes param n time
@timer
def example_func(n):
    # puts the () for n time
    time.sleep(n)

# now the example_func() is not being directly called, it goes through timer() function
example_func(10)
# example_func() this function is passed as param in the timer() function

print("waited for 15 second")