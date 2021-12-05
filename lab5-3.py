user_input = int(input("Enter any number: "))

if user_input < 0:
    print("The entered number is negative.")
elif user_input > 0:
    print("The entered number is positive.")
elif user_input == 0:
    print("The given number is zero.")
else:
    print("Please enter atleast number.")