"""The program should read three integers: the number of students in each of the three

classes, a, b and c respectively.

Suppose In the first test there are three groups. The first group has 20 students and thus needs 10

desks. The second group has 21 students, so they can get by with no fewer than 11 desks.

11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

    """
Class_A = int(input("Enter the number of the students of class A: "))
Class_B = int(input("Enter the number of the students of class B: "))
Class_C = int(input("Enter the number of the students of class C: "))

desk_required = (Class_A // 2 + Class_B // 2 + Class_C // 2 + Class_A % 2 + Class_B % 2 + Class_C % 2)
print(f"The total desk required is {desk_required}")


