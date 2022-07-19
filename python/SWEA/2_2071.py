import sys

sys.stdin = open("input/2_2071_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num = input().split()
    sum = 0
    cnt = 0
    ave = 0
    for i in num:
        sum += int(i)
        cnt += 1
    ave = sum / cnt
    print(f'#{test_case} {round(ave)}')
    # ///////////////////////////////////////////////////////////////////////////////////
