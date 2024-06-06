# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

def check_ripeness(fruit, color):
    # Define ripeness conditions for different fruits
    ripeness_conditions = {
        "banana": {
            "green": "Unripe",
            "yellow": "Ripe",
            "brown": "Overripe"
        },
        "apple": {
            "green": "Unripe",
            "red": "Ripe",
            "yellow": "Ripe",
            "brown": "Overripe"
        },
        "avocado": {
            "green": "Unripe",
            "dark green": "Ripe",
            "black": "Ripe",
            "brown": "Overripe"
        }
    }

    # Check if the fruit is in the ripeness conditions dictionary
    if fruit in ripeness_conditions:
        # Check if the color is in the fruit's ripeness dictionary
        if color in ripeness_conditions[fruit]:
            return ripeness_conditions[fruit][color]
        else:
            return "Unknown color"
    else:
        return "Unknown fruit"

# Get input from the user
fruit = input("Enter the fruit name: ").lower()
color = input("Enter the color of the fruit: ").lower()

# Determine the ripeness
ripeness = check_ripeness(fruit, color)

# Print the result
print(f"The {fruit} is {ripeness}.")
