## input
numbers = [0, 20, 110, 50, -60, 50, 100]
max = numbers[0]

for i in numbers :
    for j in numbers :
        if(j < i):
            continue
        elif(max < i):
            max = i
        else:
            continue
print(max)