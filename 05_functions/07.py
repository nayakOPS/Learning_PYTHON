""" 7. Function with *args
Problem: Write a function that takes variable number of arguments and returns their sum. """

def sum_all(*args):
    print("Args as Tuples",args) #returns tuple
    for i in args:
        print(i * 2)
    print("default param",*args) #retuns arguments passed
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,6,3,5,6))
print(sum_all(1,2,34,5))
    
