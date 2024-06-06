# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

def customize_coffee(size, extra_shot=False):
    order = size + " coffee"
    if extra_shot:
        order += " with extra shot"
    return order

# Example usage:
size = input("Enter the size of your coffee (Small/Medium/Large): ").capitalize()
extra_shot_input = input("Do you want an extra shot of espresso? (yes/no): ").lower()

if extra_shot_input == "yes":
    extra_shot = True
else:
    extra_shot = False

coffee_order = customize_coffee(size, extra_shot)
print("Your coffee order is:", coffee_order)
