
def counta(word):
    cnt = 0
    for w in word:
        if (w == 'a'):
            cnt += 1
    print(f'{word}에서 a의 개수는 : {cnt}')

counta('apple')
counta('banana')
counta('kiwi')
