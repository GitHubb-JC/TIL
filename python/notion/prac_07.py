## input
numbers = [-10, -100, -30] # -100
min = numbers[0]

for i in numbers :
    if(min > i):
        min = i
    else:
        i = i
print(min)