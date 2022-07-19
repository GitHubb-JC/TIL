import sys

sys.stdin = open("input/3_2070_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a, b = input().split()
    if int(a) < int(b):
        print(f'#{test_case} <')
    elif int(a) > int(b):
        print(f'#{test_case} >')
    else:
        print(f'#{test_case} =')
    # ///////////////////////////////////////////////////////////////////////////////////
