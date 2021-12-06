"""
 Write a Python program to sum three given integers. However, if two or more values are

equal sum will be zero.

"""

input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))
input_3 = int(input("Enter the third number: "))

if (input_1 == input_2) or (input_2 == input_3):
    print("Zero")

else: 
    print("sum: ", input_1+input_2+input_3)