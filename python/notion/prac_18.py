def alpha_num(word):
    alp_n = {}
    for w in word:
        alp_n[w] = 0
    for w in word:
        alp_n[w] = alp_n.get(w) + 1
    for w in alp_n:
        print(f'{w} {alp_n[w]}')

alpha_num('banana')
