# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

def suggest_activity(weather):
    # Convert the weather input to lowercase for case-insensitive comparison
    weather = weather.lower()

    # Check the weather condition and suggest an activity accordingly
    if weather == "sunny":
        return "Go for a walk"
    elif weather == "rainy":
        return "Read a book"
    elif weather == "snowy":
        return "Build a snowman"
    elif weather == "cloudy":
        return "Take photographs"
    elif weather == "windy":
        return "Fly a kite"
    elif weather == "stormy":
        return "Stay indoors and watch a movie"
    else:
        return "Unknown weather condition"

# Get input from the user
weather = input("Enter the weather condition: ")

# Suggest an activity
activity = suggest_activity(weather)

# Print the result
print(f"Since it is {weather}, you should: {activity}.")
