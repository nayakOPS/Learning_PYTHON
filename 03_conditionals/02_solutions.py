# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

user_age = int(input("Enter your age : "))

def get_day_of_week(number):
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"

user_input_day = int(input("Enter a number (1-7) to choose the day of the week: "))
selected_day = get_day_of_week(user_input_day)

# print(selected_day)

# make the price $12 if the age >= 18 otherwise make the price 8
price = 12 if user_age >= 18 else 8

if selected_day == "Wednesday":
    price = price -2 
    print("ON Wednesday $2 DISCOUNT, The Ticket Price is $",price)
else:
    print("The Ticket Price is $",price)