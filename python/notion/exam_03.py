numbers = input().split()

numbers_int = []
for n in numbers:
    numbers_int.append(int(n))
    
print(sum(numbers_int))