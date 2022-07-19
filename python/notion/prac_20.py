# input
number = 123
i = 0
sum = 0

while number >= 1:
    sum += number % 10
    number = int(number / 10)
    i += 1
print(sum)

