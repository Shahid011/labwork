"""
Write a program to print absolute vlaue of a number entered by user. E.g.-

INPUT: 1        OUTPUT: 1

INPUT: -1        OUTPUT: 1
"""

user_input = int(input("Enter any integer for absolute value: "))

absolute_value = abs(user_input)

print(f"Absolute value of {user_input} is {absolute_value}")