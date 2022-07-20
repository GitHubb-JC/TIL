import sys

sys.stdin = open("input/8_1284_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    p, q, r, s, w = map(int, input().split())

    a_price = p * w
    
    if w <= r:
        b_price = q
    else:
        b_price = q + (s * (w - r))

    if a_price < b_price:
        print(f'#{test_case} {a_price}')
    else:
        print(f'#{test_case} {b_price}')
    # ///////////////////////////////////////////////////////////////////////////////////
