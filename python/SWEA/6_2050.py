import sys

sys.stdin = open("input/6_2050_input.txt", "r")

T = input()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in T:
    # ///////////////////////////////////////////////////////////////////////////////////
    print(ord(test_case)-64, end=' ')
    # ///////////////////////////////////////////////////////////////////////////////////
