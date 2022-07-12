n = int(input())
i = 1
sum = 1

while i <= n:
    sum *= i
    i += 1
print(sum)

i = 1
sum = 1

for i in range(n) :
    i += 1
    sum *= i
print(sum)