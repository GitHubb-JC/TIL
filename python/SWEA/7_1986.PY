import sys

sys.stdin = open("input/7_1986_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    sum = 0
    T_num = int(input())
    for n in range(1, T_num + 1):
        if n % 2 == 1:
            sum += n
        else:
            sum -= n
    print(f'#{test_case} {sum}')
    # ///////////////////////////////////////////////////////////////////////////////////
