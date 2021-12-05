"""find BMI of a person where take mass and height as input from the user

BMI=mass in kg / (height in m)2
"""


mass = float(input("Enter the mass: "))
height = float(input("Enter the height: "))

BMI = mass / height**2

print(f"The BMI of given mass and height is {BMI}kg/m\u00b2")