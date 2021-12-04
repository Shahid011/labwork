"""
 N students take K apples and distribute them among each other evenly. The remaining

(the indivisible) part remains in the basket. How many apples will each single student

get? How many apples will remain in the basket? The program reads the numbers N and

K. It should print the two answers for the questions above.
"""

num_student = int(input("Enter the number of students: "))
num_apples = int(input("Enter the number of apples: "))

evenly_distributed = num_apples // num_student
remaining_apples = num_apples % num_student

print(f"{num_student} students will get {evenly_distributed} apples when distributed evenly. ")
print(f"{remaining_apples} apples will remain in basket while distributed evenly among {num_student} students ")