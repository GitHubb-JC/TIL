def posi_a(word):
    posi = 0
    print(f'{word} 에서 a 가 등장하는 위치는 : ', end = '')
    for w in word:
        if w == 'a':
            print(posi, end = ' ')
        posi += 1
    print('이다.')

posi_a('HappyHacking')
posi_a('bananan')
posi_a('apple')
posi_a('kiwi')
posi_a('fdsa')