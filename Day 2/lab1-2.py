    #convert seconds to day, hours minutes and seconds


end_user = int(input("Enter seconds to convert it into day: "))

day = (((end_user /60) /60) /24)
hour = ((end_user/60)/60)
minute = (end_user/60)

print(f"Total day for given seconds: {day}")
print(f"Total hours for given seconds: {hour}")
print(f"Total minutes for given seconds: {minute}")



