def count_vowel(word):
    cnt = 0
    for w in word:
        if w == 'a':
            cnt += 1
        elif w == 'e':
            cnt += 1
        elif w == 'i':
            cnt += 1
        elif w == 'o':
            cnt += 1
        elif w == 'u':
            cnt += 1
    print(f'{word}에서 모음의 개수는 : {cnt}')

count_vowel('apple')
count_vowel('banana')
count_vowel('kiwi')
count_vowel('aeiou')
count_vowel('zxcvb')
