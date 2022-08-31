T = input()
for i in range(1, int(T) + 1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a + b}')