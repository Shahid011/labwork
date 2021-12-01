num = int(input("print sum of odd numbers till: "))
sum = 0

for i in range(1, num+1):
    if(not(i%2)==0):
        sum += i

print(f"The sum of first {num} odd number is {sum}")