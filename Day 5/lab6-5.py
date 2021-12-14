numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
odd_count = 0
even_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    elif number % 2 != 0:
        odd_count += 1
    else:
        pass
print(f"Odd Count: {odd_count} and Even Count: {even_count} ")