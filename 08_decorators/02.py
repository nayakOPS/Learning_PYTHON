# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        # iterating the list of args and converting the individual arg ko string
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}:{v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper
# returning definition reference of the wrapper function


@debug
def greet(name, greeting="Namaste"):
    print(f"{greeting}, {name}")


greet("Daju","Namaste");


# A basic decorator looks like this

""" def debug(func):
    def wrapper():
        return func()
    return wrapper

@debug
def hello():
    print("Hello World") """