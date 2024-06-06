# Problem: Given a string, find the first non-repeated character.

# break will skip the whole iteration after the conditon has been met

input_str = "teeteracasdaf"

for char in input_str:
    print("The loop running at :",char)
    if input_str.count(char) == 1:
        print("char is:", char)
        break
