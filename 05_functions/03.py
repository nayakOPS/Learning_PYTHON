""" 3. Polymorphism(one function different work ) in Functions 
Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings. """

def multiply(p1,p2):
    val = p1 * p2
    return val

print(multiply(9,7))
print(multiply("h",7))
print(multiply(9,"a"))