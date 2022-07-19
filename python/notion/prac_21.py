# input
number = 1234
num = []

while number >= 1:
    num.append(number % 10)
    number = int(number / 10)

# print(num)
str_r = num[::-1]
# print(str_r)

num_r = 0
i = 1

for n in str_r:
    num_r += n * i
    i *=10

print(num_r)