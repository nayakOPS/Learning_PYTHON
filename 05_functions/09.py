""" 9. Generator Function with yield
Problem: Write a generator function that yields even numbers up to a specified limit. """

def even_generator(limit):
    for i in range(2, limit+1, 2):
        # return i  this returns 2 and exit
        # yield stores the state of the function
        yield i
        #for every instance of i it hold in memory and returns it 

""" r = even_generator(10)
print(r) returns ==> <generator object even_generator at 0x000001F79E5E92A0> """

for num in even_generator(10):
    print(num)