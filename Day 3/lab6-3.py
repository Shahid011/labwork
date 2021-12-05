"""
    Given an integer number, print its last digit. 
"""

user_input = int(input("Enter an integer: "))

last_digit = user_input % 10

print(f"{last_digit} is the last digit of the given integer.")