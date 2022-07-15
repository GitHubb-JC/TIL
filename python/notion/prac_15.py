def posi_a(word):
    posi = 0
    for w in word:
        if w == 'a':
            print(f'{word} 에서 a 가 처음으로 등장하는 위치(index)는 : {posi} 이다.')
            break
        posi += 1
        if posi == len(word):
            print(f'{word} 에서 a 가 처음으로 등장하는 위치(index)는 : -1 이다.')


posi_a('bananan')
posi_a('apple')
posi_a('kiwi')
posi_a('fdsa')