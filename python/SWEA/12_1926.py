import sys

sys.stdin = open("input/12_1926_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    cnt = 0
    for i in str(test_case):
        i = int(i)
        if i == 3 or i == 6 or i == 9:
            cnt += 1
        else:
            cnt += 0
    #print(f'({cnt})', end=' ')
    if cnt == 0:
        print(test_case, end='')
    else:
        for n in range(1, cnt + 1):
            print('-', end='')
    print('', end=' ')


    # ///////////////////////////////////////////////////////////////////////////////////
