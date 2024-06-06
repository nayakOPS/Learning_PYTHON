# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time

# designing decorator

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a,b):
    time.sleep(4)
    # imagine scenario like in this 4 seconds time, we are communicating with server to get value of a,b and in the decorator we are putting the extracted value in cache
    return a+b

print(long_running_function(2,3)) #at this time the values are not found in cache so empty {} cache is returned
print(long_running_function(2,3)) #the reuqested args is found in cache and from the args the value is calculated
print(long_running_function(4,3))
print(long_running_function(4,3))