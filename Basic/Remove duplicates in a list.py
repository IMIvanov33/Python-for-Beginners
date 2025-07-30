numbers = [2, 2, 4, 4, 1, 3, 5, 5, 6]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)
