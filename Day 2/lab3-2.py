""" Given the integer N - the number of minutes that is passed since midnight - how many

hours and minutes are displayed on the 24h digital clock?

The program should print two numbers: the number of hours (between 0 and 23) and the

number of minutes (between 0 and 59).

For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30

am. So, the program should print 2 30.
    """
minutes_passed = int(input("Enter the number of minutes passed since mid-night: "))


hours = minutes_passed // 60

minutes = minutes_passed % 60

print(f"{hours}: {minutes}")