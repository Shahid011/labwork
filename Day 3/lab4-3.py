"""4. Given three integers, print the smallest one. (Three integers should be user input) 
"""
user_input_1 = int(input("Enter the 1st integer: "))
user_input_2 = int(input("Enter the 2nd integer: "))
user_input_3 = int(input("Enter the 3rd integer: "))

if (user_input_1 <= user_input_2 and user_input_1 <= user_input_3):
    print(user_input_1, "is the smallest.")
elif (user_input_2 <= user_input_1 and user_input_2 <= user_input_3):
    print(user_input_2, "is the smallest")
else:
    print(user_input_3, "is the smallest.")