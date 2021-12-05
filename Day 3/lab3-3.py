"""
    3. Check whether the user input number is even or odd and display it to user. 

"""

user_input = int(input("Enter any number: "))

if user_input % 2 == 0:
    print(f"{user_input} is even number")
elif not(user_input%2==0):
    print(f"{user_input} is odd number")

else:
    print("Please enter number except 0")