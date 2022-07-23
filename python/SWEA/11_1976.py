import sys

sys.stdin = open("input/11_1976_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tnum = map(int, input().split())
    tnum = list(tnum)
    # print(tnum)
    time = tnum[0] + tnum[2]
    minute = tnum[1] + tnum[3]
    if minute > 60:
        minute = minute - 60
        time += 1
    if time > 12:
        time = time - 12
    print(f'#{test_case} {time} {minute}')
    # ///////////////////////////////////////////////////////////////////////////////////
