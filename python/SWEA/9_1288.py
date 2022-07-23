import sys

sys.stdin = open("input/9_1288_sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    mult = int(input())
    num = 0
    i = 1
    s = set()
    while len(s) <= 9:
        num = mult * i
        i += 1
        #print(str(num))
        for n in str(num):
            #print(n)
            s.add(n)
    print(f'#{test_case} {num}')
    # ///////////////////////////////////////////////////////////////////////////////////
