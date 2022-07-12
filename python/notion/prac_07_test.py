## input
numbers = [0, 20, 100, 50, -60, 50, -100] # 50
min = numbers[0]
i = 0
n = len(numbers)

for i in numbers :
    for j in numbers :
        if(j > i):
            continue
        elif(min > i):
            min = i
        else:
            continue
print(min)