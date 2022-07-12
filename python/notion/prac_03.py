n = int(input())
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1
print(sum)

i = 1
sum = 0

for i in range(n + 1) :
    sum += i
print(sum)
