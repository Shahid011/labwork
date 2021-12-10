"""
A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user

Number of classes held

Number of classes attended.

And print

percentage of class attended

Is student is allowed to sit in exam or not
"""

input_1 = int(input("Number of class held: "))
input_2 = int(input(("Number of class attend: ")))

print(f"Total classes held till date:{input_1}.")
print(f"You attend {input_2} out of {input_1} classes.")

percentage = round(input_2 / input_1 * 100)

print(f"Your percentage is {percentage}%")

if percentage < 75:
    print("You are not allowed to sit in exam. ")
else:
    pass