user_age = int(input("Enter your age : "))

if user_age <= 13 and user_age >= 1:
    print("The User is Child")
elif user_age >= 13 and user_age <=19:
    print("The user is Teenager")
elif user_age >= 20 and user_age <=59:
     print("The user is Adult")
elif user_age >= 60 and user_age <=110:
    print("The user is Senior")
else:
    print("Invalid Age")