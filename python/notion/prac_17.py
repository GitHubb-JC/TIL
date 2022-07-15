def change_Big(word):
    cb = ''
    for w in word:
        asc = ord(w)
        if 97 <= asc <= 122:
            asc -= 32
            cb += (chr(asc))
    print(cb)

change_Big('banana')