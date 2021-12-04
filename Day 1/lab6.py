num = int(input("print sum of even numbers till: "))
sum = 0

for i in range(1, num+1):
    if(i % 2 == 0):
        sum += i

print(f"The sum of first {num} even number is {sum}")