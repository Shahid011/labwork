"""
7. Given a positive real number, print its fractional part.
"""
user_input = float(input("Enter a positive real number: "))

fractional_part = user_input - int(user_input)

print(f"{fractional_part} is the fractional part of the given positive real number")