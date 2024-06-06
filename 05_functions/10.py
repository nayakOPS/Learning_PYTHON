# Problem: Create a recursive function to calculate the factorial of a number.

def fact_num(n):
    if n == 0:
        return 1
    else:
        return n * fact_num(n-1)
    
fact = fact_num(10)
print(fact)
