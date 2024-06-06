# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# Get the input from the user and split it into two parts
input_values = input("Enter the number to find the table upto 10th and Enter the skipping Iteration number respectively: ").split(" ")

num = int(input_values[0])
skip_num = int(input_values[1])  if(len(input_values) > 1) else None

for i in range(1,11):
    if i==skip_num:
        # in continue only one iteration is skipped
        # what continue does that it skips the current instance and runs the process
        # so here the 5th iteration is skipped
        continue
    print(num, 'x', i, '=', num*i)
