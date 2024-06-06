""" 8. Function with **kwargs
Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value. """

# key words arguements = kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="superman")
print_kwargs(name="Ben10", power="watch", enemy = "Alien")