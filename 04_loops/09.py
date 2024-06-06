# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

# set() only contains unique values , if values are duplicate then not select the item
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate Item: ", item)
        break
    unique_item.add(item)
