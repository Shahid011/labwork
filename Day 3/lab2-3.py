"""2. WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
"""

programming_algorithm = float(input("Enter the mark of programming and algorithm: "))
software_design = float(input("Enter the mark of software design: "))
mathematics = float(input("Enter the mark of mathematics: "))
led_1 = float(input("Enter the mark of led 1: "))
total_marks = 400
marks_obtained = programming_algorithm + software_design + mathematics + led_1

percentage = marks_obtained / total_marks * 100

print(f"You obtained {percentage} %")

if percentage > 70:
    print("congratulation!! you passed with distinctions marks")

elif percentage > 60:
    print("Congratulations you passed with 1st division")

elif percentage > 40:
    print("you passed with 2nd divison")
elif percentage < 40:
    print("Sorry you had fail, please try again!")

