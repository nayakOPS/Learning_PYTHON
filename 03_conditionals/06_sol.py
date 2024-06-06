# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

def choose_transportation(distance):
    if distance < 3:
        return "Walk"
    elif 3 <= distance <= 15:
        return "Bike"
    else:
        return "Car"

# Example usage:
distance = float(input("Enter the distance in kilometers: "))

transportation_mode = choose_transportation(distance)
print("Your mode of transportation is:", transportation_mode)
