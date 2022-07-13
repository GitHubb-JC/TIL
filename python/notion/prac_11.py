
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = 0

for i in numbers:
    if i >= 2:
        print(f'{i} 단')
        for j in numbers:
            res = i * j
            print(f'{i} X {j} = {res}')