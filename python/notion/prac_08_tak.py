numbers = [110, 20, 100, 40]
max_number = numbers[0]
second_number = numbers[0]

for n in numbers:
    if max_number < n:
        second_number = max_number
        max_number = n
    elif second_number < n and n < max_number:
        second_number = n
print(second_number)
