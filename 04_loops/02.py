# Problem: Calculate the sum of even numbers up to a given number n.

num = int(input("Enter the number to till for counting the sum of even number: "))

sum_even = 0

for i in range(1, num+1):
    if i%2==0:
        sum_even +=1
print("The sum of even numbers upto the given number is : ",sum_even)