# Problem: Compute the factorial of a number using a while loop.

# 5 ! = 5*4*3*2*1

number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1
    # factorial = factorial * number
    # number = number - 1

print("Factorial : ", factorial)