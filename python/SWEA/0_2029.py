
import sys

sys.stdin = open("input/0_2029_input.txt", "r")

T = input()

ans = 0
nm = 0

for i in range(int(T)):
    a, b = input().split()
    ans = int(a) / int(b)
    nm = int(a) % int(b)
    print(f'#{i + 1} {int(ans)} {int(nm)}')