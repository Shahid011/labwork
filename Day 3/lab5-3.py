"""
For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0. 
"""



user_input = int(input("Enter any number: "))

if user_input > 0:
    print("True")
elif user_input < 0:
    print("False")
elif user_input == 0:
    print("Zero")
else:
    print("Please enter atleast number.")