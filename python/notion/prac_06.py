## input
numbers = [-10, -100, -30] # -10 
max = numbers[0]

for i in numbers :
    if(max < i):
        max = i
    else:
        i = i
print(max)