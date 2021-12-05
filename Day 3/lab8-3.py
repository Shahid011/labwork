"""
    Given a n-digit number. Find the sum of its digits
"""

my_list = []

user_input = int(input("Enter the number of numbers in my list: "))

for i in range(0, user_input):
    elements = int(input())
    my_list.append(elements)

sum = sum(my_list)

print(f"The sum is {sum}")