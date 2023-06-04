# Car Rental Amount

print("Welcome to the Car Rental Store")

age = int(input("Please enter your age: "))

first_timer = input("Is it your first time renting a car with our company?\nEnter Y or N: ")

rental_duration = int(input("For how many days would you like to rent our car? "))

if age >= 60:
    print("Thank you, you are eligible for a 60 % discount")

elif age < 25:
    if first_timer.lower() == 'y':
        print("Thank you, you are eligible for a 15 % discount")

    elif first_timer.lower() == 'n':
        print("Thank you, you are eligible for a 20 % discount")

else:
    if rental_duration > 7:
        print("Thank you, you are eligible for a 5 % discount")

    else:
        print("Sorry, you are not eligible for any discount.")

        


